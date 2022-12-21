from botcity.web import WebBot, Browser
from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
from botcity.maestro import *
import BancoDados
import Paths
import NavWeb
import ConcatePlan

class Bot(WebBot):
    def action(self, execution=None):

        #   desktop_bot = DesktopBot()
        n = 0
        while(n<4):
            linha = BancoDados.FilaBanco()
            if(linha):
                linha = linha[0]
                BancoDados.attFila('Executando',linha[1],linha[2],linha[3])
                path_pasta = Paths.createPaths(linha[2],linha[3],linha[1])
                NavWeb.navWeb(path_pasta,linha[4],linha[5])
                Paths.renameFile(path_pasta,linha[1],linha[2],linha[3])
                BancoDados.attFila('Sucesso',linha[1],linha[2],linha[3])

            if not(linha):
                ConcatePlan.ConcatenarPlanilhas(Paths.createBase())
            n+=1
        '''
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Configure whether or not to run on headless mode
        #self.headless = False

        # Instantiate a DesktopBot
        #desktop_bot = DesktopBot()
        # Execute operations with the DesktopBot as desired
        # desktop_bot.control_a()
        # desktop_bot.control_c()
        # desktop_bot.get_clipboard()

        # Uncomment to change the default Browser to Firefox
        # self.browser = Browser.FIREFOX

        # Uncomment to set the WebDriver path
        # self.driver_path = "<path to your WebDriver binary>"

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        #self.browse("https://www.botcity.dev")

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

        # Wait for 10 seconds before closing
        #self.wait(10000)

        # Stop the browser and clean up
        #self.stop_browser()

        self.maestro.finish_task(
            task_id=execution.task_id,
            status=AutomationTaskFinishStatus.SUCCESS,
            message="Task Finished OK."
        )
        '''

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
