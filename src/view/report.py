from matplotlib.backends.backend_pdf import PdfPages
from pathlib import Path
from .figure import Figure


class Report:
    def __init__(self, output_dir="assets"):
        self.figures = []
        self.output_dir = Path(output_dir)

    def new_figure(
        self, title=None, figSize=(10, 7), ncols=1, nrows=1, fontsize=13
    ) -> Figure:
        fig = Figure(title, figSize, ncols, nrows, fontsize)
        self.figures.append(fig)
        return fig

    def save(self, filename):
        with PdfPages(self.output_dir / filename) as pdf:
            for fig in self.figures:
                fig.save(pdf=pdf)

    def append_figures(self, figures):
        self.figures += figures
