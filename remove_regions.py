import sublime, sublime_plugin


class RemoveRegionsCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        regions = len(view.sel())
        # default = view.settings().get("remove_regions_string", "")

        self.window.show_input_panel("Regions to remove ({0} active):".format(regions), "", self.on_done, None, None)
        pass

    def on_done(self, text):
        if len(text) < 1:
            return
        if self.window.active_view():
            self.window.active_view().run_command('remove_regions_do', {'r': text})

class RemoveRegionsDoCommand(sublime_plugin.TextCommand):
    def run(self, edit, r):
        regions = []

        self.view.settings().set("remove_regions_string", r)

        if r == "odd" or r == "even":
            idx = self.get_odd_even(r == "odd")
        else:
            idx = self.get_index(r)

        i = 0
        for s in self.view.sel():
            if not i in idx:
                regions.append(s)
            i = i + 1

        self.view.sel().clear()
        for r in regions:
            self.view.sel().add(r)

    def get_index(self, r):
        idx = []
        for item in r.split(","):
            if item.find("-") != -1 :
                for i in range(int(item.split("-")[0].strip()), int(item.split("-")[1].strip())+1):
                    idx.append(i)
            else:
                idx.append(int(item.strip()))

        return idx

    def get_odd_even(self, odd):
        idx = []
        for i in range(len(self.view.sel())):
            if (not odd and i % 2 == 0) or (odd and i % 2 > 0):
                idx.append(i)
        return idx

class RemoveRegionsOdd(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("remove_regions_do", {"r": "odd"})

class RemoveRegionsEven(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("remove_regions_do", {"r": "even"})

class RemoveRegionsAgain(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        r = view.settings().get("remove_regions_string", "")
        if not r == "":
            view.run_command("remove_regions_do", {"r": r})
