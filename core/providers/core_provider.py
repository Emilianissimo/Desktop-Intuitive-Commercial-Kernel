"""
    CLASS CoreProvider have to be used in case with interfering to moment until page loaded.
    So here, you can see, that I'm using it to re-render data each time, when I'm opening page.
    For better optimisation performance you can disable it, but if you will change data, it wouldn't be shown.
    It wouldn't be a problem for modern computers.
"""


class CoreProvider:
    @staticmethod
    def boot(widget):
        widget.render_data()
