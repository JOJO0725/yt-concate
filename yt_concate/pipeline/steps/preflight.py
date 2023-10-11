from .step import Step

class Preflight(Step):
# 在下載影片字幕前,建立自料夾裝載影片跟字幕
    def process(self, data, inputs, utils):
        print('in Preflight')
        utils.create_dirs()
