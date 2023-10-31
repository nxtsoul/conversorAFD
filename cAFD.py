from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from cAFD_UI import Ui_ConversorAFD
from unicodedata import normalize
from pathlib import Path
import sys, re, os, subprocess

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_ConversorAFD()
        self.ui.setupUi(self)
        self.appdata = os.path.join(os.getenv('APPDATA'), 'GERAFD')
        self.file_default = os.path.join(self.appdata, 'default.ini')
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            self.currentDirectory = sys._MEIPASS
        else:
            self.currentDirectory = os.path.abspath(os.getcwd())
        self.windowIcon = os.path.join(self.currentDirectory, 'cAFD.ico')
        self.setWindowIcon(QtGui.QIcon(self.windowIcon))
        if os.path.exists(self.file_default):
            f = open(self.file_default, 'r')
            self.razaosocial, self.cnpj, self.mte = f.read().split(',')
            self.autoCompletaCampo()
        else:
            self.razaosocial, self.cnpj, self.mte = None, None, None
        self.ui.box_START.released.connect(self.trataDados)
        self.ui.box_QUIT.released.connect(self.sairDoApp)
        self.ui.box_FILE_BUTTON.released.connect(self.selecionaArquivo)
        self.fileName = None

    def autoCompletaCampo(self):
        self.ui.box_RAZAOSOCIAL_INPUT.setText(self.razaosocial)
        self.ui.box_CNPJ_INPUT.setText(self.cnpj)
        self.ui.box_MTE_INPUT.setText(self.mte)
    
    def selecionaArquivo(self):
        home_dir = str(Path.home())
        self.fname = QFileDialog.getOpenFileName(self, 'Selecione o arquivo AFD', home_dir, 'Arquivo AFD (*.txt)')
        self.fileName = self.fname[0]
        self.ui.box_FILE_INPUT.setText(Path(self.fname[0]).name)
    
    def salvaArquivo(self):
        home_dir = str(Path.home())
        joinedt = os.path.join(home_dir, f'AFD_{self.ui.box_MTE_INPUT.text()}')
        self.savefname = QFileDialog.getSaveFileName(self, 'Salvar o arquivo AFD gerado', joinedt, 'Arquivo AFD (*.txt)')
        self.saveFileName = self.savefname[0]
        if self.saveFileName != None:
            return self.saveFileName
        else:
            return False
    
    def sairDoApp(self):
        sys.exit(1)
    
    def showWarning(self, title, message):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setWindowTitle(title)
        msgbox.setWindowIcon(QtGui.QIcon(self.windowIcon))
        msgbox.setText(message)
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec()
        return None
    
    def showQuestion(self, title, message):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Question)
        msgbox.setWindowTitle(title)
        msgbox.setWindowIcon(QtGui.QIcon(self.windowIcon))
        msgbox.setText(message)
        msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgbox.button(msgbox.Yes).setText("Sim")
        msgbox.button(msgbox.No).setText("Não")
        return msgbox.exec()
    
    def showInformation(self, title, message):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle(title)
        msgbox.setWindowIcon(QtGui.QIcon(self.windowIcon))
        msgbox.setText(message)
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.exec()
        return None
    
    def trataDados(self):
        input_box = self.ui.box_RAZAOSOCIAL_INPUT.text()
        input_box_cnpj = self.ui.box_CNPJ_INPUT.text()
        input_box_mte = self.ui.box_MTE_INPUT.text()
        if len(input_box) < 1:
            self.showWarning("Campo em branco", "O campo de Razão social não pode ser deixado em branco, verifique e tente novamente.")
            return False
        elif len(input_box) > 1 and len(input_box) < 5:
            self.showWarning("Razão social inválida", "A razão social deve constar entre 10 e 150 caracteres, verifique e tente novamente.")
            return False
        if len(input_box_cnpj) < 1:
            self.showWarning("Campo em branco", "O campo CNPJ não pode ser deixado em branco, verifique e tente novamente.")
            return False
        elif len(input_box_cnpj) > 1 and len(input_box_cnpj) < 14:
            self.showWarning("Numeração CNPJ inválida", f"A numeração CNPJ contém 14 digitos, você digitou apenas {len(input_box_cnpj)} dígitos, verifique e tente novamente.")
            return False
        if len(input_box_mte) < 1:
            self.showWarning("Campo em branco", "O campo de Número de Registro MTE do REP não pode ser deixado em branco, verifique e tente novamente.")
            return False
        elif len(input_box_mte) > 1 and len(input_box_mte) < 17:
            self.showWarning("Numeração MTE inválida", f"A numeração de registro MTE contém 17 digitos, você digitou apenas {len(input_box_mte)} dígitos, verifique e tente novamente.")
            return False
        
        if self.fileName == None or self.fileName == "":
            self.showWarning("Nenhum arquivo selecionado", f"Nenhum arquivo AFD foi selecionado, verifique e tente novamente.")
            return False
        
        if self.fname[0]:
            self.fileName = self.fname[0]
            if os.path.exists(self.fileName):
                if self.fileName.split('.')[-1].lower() != "txt":
                    self.showWarning("Extensão inválida", f'O arquivo selecionado não é um arquivo AFD válido, os arquivos AFD costumam ter a extensão "*.txt" e o arquivo selecionado contém a extensão "*.{self.fileName.split(".")[-1].lower()}", verifique e tente novamente.')
                    return False
            else:
                self.showWarning("O arquivo selecionado não existe", f'O arquivo selecionado "{Path(self.fname[0]).name}" não existe, talvez tenha sido movido ou excluído, verifique e tente novamente.')
                return False
        
        process = normalize('NFKD', input_box.upper()).encode('ASCII', 'ignore').decode('ASCII')
        process = re.sub(r'[?|$|.|!]', '', process)
        self.ui.box_RAZAOSOCIAL_INPUT.setText(process)
        if not os.path.exists(self.appdata):
            os.mkdir(self.appdata)
        if not os.path.exists(self.file_default):
            f = open(self.file_default, 'w')
            f.write(f"{process},{input_box_cnpj},{input_box_mte}")
            f.close()
        else:
            os.unlink(self.file_default)
            f = open(self.file_default, 'w')
            f.write(f"{process},{input_box_cnpj},{input_box_mte}")
            f.close()
        self.processaAFD(self.fileName)

    def processaAFD(self, arquivo):
        def trataMarcacoes(marc):
            nsr = marc[0:9]
            tipo_marc = marc[10]
            data_marc = marc[10:18]
            hora_marc = marc[18:22]
            pis_marc = marc[22:34]
            crc16_marc = marc[34:38]
            return [nsr, tipo_marc, data_marc, hora_marc, pis_marc, crc16_marc]

        def coletaDataInicialeFinalParaCabecalhoAFD(arquivo):
            marcacoes = []
            conteudo = None
            with open(arquivo, 'r') as f:
                conteudo = f.readlines()
            for x in conteudo:
                x = x.replace('\n', '')
                if len(x) == 38:
                    marcacoes.append(x)
            primeira_marc = marcacoes[0]
            ultima_marc = marcacoes[len(marcacoes)-1]
            return [marcacoes, len(marcacoes), trataMarcacoes(primeira_marc)[2], trataMarcacoes(ultima_marc)[2], trataMarcacoes(ultima_marc)[2], trataMarcacoes(ultima_marc)[3]]

        def formataRazaoSocialAFD(string):
            if len(string) == 150:
                return string
            elif len(string) > 150:
                return string[0:150]
            elif len(string) < 150:
                afd_format = 150-len(string)
                return string+" "*afd_format

        def trataMarcacoesRodape(contagem):
            cont_marc = 9-len(str(contagem))
            return "0"*cont_marc+str(contagem)

        tipo_registro_cabecalho_AFD = "1"
        ref_cabecalho_n = "0"*9
        ref_rodape_n = "9"*9
        tipo_empregador_AFD = "1"
        ref_cod_trailer = "9"
        cnpj_empregador_AFD = self.ui.box_CNPJ_INPUT.text()
        cei_empregador_AFD = "0"*12
        razao_social_AFD = self.ui.box_RAZAOSOCIAL_INPUT.text()
        numero_mte_relogio_AFD = self.ui.box_MTE_INPUT.text()
        marcacoes_AFD, contagem_marcacoes, data_inicial_batidas_AFD, data_final_batidas_AFD, data_geracao_arquivo_AFD, hora_geracao_arquivo_AFD = coletaDataInicialeFinalParaCabecalhoAFD(arquivo)


        header_AFD = f"{ref_cabecalho_n}{tipo_registro_cabecalho_AFD}{tipo_empregador_AFD}{cnpj_empregador_AFD}{cei_empregador_AFD}{formataRazaoSocialAFD(razao_social_AFD)}{numero_mte_relogio_AFD}{data_inicial_batidas_AFD}{data_final_batidas_AFD}{data_geracao_arquivo_AFD}{hora_geracao_arquivo_AFD}"
        footer_AFD = f"{ref_rodape_n}{ref_cabecalho_n}{trataMarcacoesRodape(contagem_marcacoes)}{ref_cabecalho_n*3}{ref_cod_trailer}"

        salvaArquivo_ = self.salvaArquivo()
        if salvaArquivo_ == False or salvaArquivo_ == "":
            self.showWarning("Nenhum local definido", "Nenhum local foi definido para salvar o arquivo, tente novamente.")
            return False

        if os.path.exists(salvaArquivo_):
            a = self.showQuestion("O arquivo já existe", f"O arquivo que você está tentando salvar já existe no local, deseja sobrescrever ?")
            if a == QMessageBox.No:
                self.showInformation("Processo cancelado", "O processo foi cancelado pelo usuário.")
                return False
        with open(salvaArquivo_, 'w') as f:
            f.write(header_AFD+'\n')
            for x in marcacoes_AFD:
                f.write(x+'\n')
            f.write(footer_AFD)
            f.close()
        a_q = self.showQuestion("Arquivo gerado com sucesso", f'Seu arquivo foi salvo em "{salvaArquivo_}", contendo {len(marcacoes_AFD)} marcações de ponto.\nDeseja abrir o arquivo agora ?')
        if a_q == QMessageBox.Yes:
            string = salvaArquivo_.replace("\\", "\\\\")
            subprocess.call(["notepad.exe", string])
        else:
            return True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())