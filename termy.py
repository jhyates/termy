# termy.py
# Termy
# This software is available under an MIT License.

from typing import List, Tuple

import domain_merge_sort as dms


class Scatter():
    def __init__(self):
        """Initialize the plotting object."""
        self.data_x = []
        self.data_y = []
        self.width = 80
        self.height = 20
        self.display = 'You must first plot data before showing it!'
        self.label_sig_figs = 3
        self.label_decimation = 5

    def plot(self, data_x: List, data_y: List, width=80, height=20) -> None:
        """Size and build the scatter plot."""
        # Make the domain monotonic increasing. This makes it easier for us to
        # Concatenate it into strings.
        data_x, data_y = dms.merge_sort(data_x, data_y)

        self.data_x = data_x
        self.data_y = data_y
        self.width = width
        self.height = height

        decimated_x, decimated_y = self._decimate()

    def show(self) -> None:
        """Display the completed scatter plot"""
        print(self.display)

    def _decimate(self) -> Tuple[List, List]:
        """Shrink the data set to fit in the desired bounds"""
        w_deci_x, w_deci_y = self._decimate_by_width()
        return w_deci_x, w_deci_y

    def _decimate_by_width(self) -> Tuple[List, List]:
        """Shrink the data set to fit in the x-bounds."""
        domain_width = len(self.data_x)
