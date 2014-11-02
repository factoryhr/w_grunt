import sublime
import sublime_plugin
import subprocess
import os
import json

class EventDump(sublime_plugin.EventListener):  
    def on_post_save(self, view):  
        self.doGrunt(view)

    def doGrunt(self, view):
        workingDir = self.getWorkingFolder(view)
        self.wd = workingDir
        self.chechForTFCConfigFile(workingDir)

    def getWorkingFolder(self, view):
        currentFileName = view.file_name()
        allFolders = view.window().folders()
        for folder in allFolders:
            if( currentFileName.find( folder ) != -1 ):
                return folder

    def runGruntCommand_terminal(self):
        sublime.active_window().active_view().set_status("tfc_grunt", "Running grunt command")
        cmd = "grunt --no-color"
        process = subprocess.Popen( {cmd}, stdout=PIPE, stderr=PIPE, env=os.environ, shell=True )
        output = process.communicate()

        print("\n\nGrunt Log\n")
        outputLine = output[0].decode("utf-8")
        print(outputLine)

        sublime.status_message("Grunt complete")

        if self.copy_to_clipboard == True:
            self.copySourcesToClipboard()

        sublime.active_window().active_view().set_status("tfc_grunt", "Grunt command finished. See console for status message")


    def chechForTFCConfigFile(self, wd):
        configFile = "%s/w_grunt.json" % (wd)

        if os.path.isfile(configFile):
            os.chdir(wd)

            if self.shouldUseGrunt(configFile):
                gruntFile = "%s/Gruntfile.js" % (wd)

                if os.path.isfile(gruntFile) == False:
                    sublime.error_message("Grunt file is not specified")
                else:
                    self.runGruntCommand_terminal()

    def shouldUseGrunt(self, configFile):

        try:
            json_data = open(configFile)

            try:
                self.options = json.load(json_data)

                if self.options["copy_to_clipboard"] == True:
                    self.copy_to_clipboard = True
                else:
                    self.copy_to_clipboard = False;

                if self.options["grunt_on_save"] == True:
                    return True
                else:
                    return False

            except ValueError as e:
                sublime.error_message("Config file is not valid JSON file. Please fix the config file!")
                return False

        except FileNotFoundError as e:
            return False

    def copySourcesToClipboard(self):
        sourceToCopy = ""

        if self.options["copy_dev_source"] == True:
            sourceToCopy = self.options["devSource"]
        else :
            sourceToCopy = self.options["productSource"]

        sourceToCopy = "%s/%s" % (self.wd, sourceToCopy)
        
        if os.path.isfile(sourceToCopy):
            rawSource = open(sourceToCopy)
            sublime.set_clipboard(rawSource.read())
        else:
            sublime.error_message("Can't find the source for copy. Destination %s" % (sourceToCopy))



