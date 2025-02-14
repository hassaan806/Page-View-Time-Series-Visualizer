import unittest
import time_series_visualizer

#testing module for time series visualizer
class TimeSeriesTestCase(unittest.TestCase):
    def test_line_plot(self):
        fig = time_series_visualizer.draw_line_plot()
        self.assertIsNotNone(fig)

    def test_bar_plot(self):
        fig = time_series_visualizer.draw_bar_plot()
        self.assertIsNotNone(fig)

    def test_box_plot(self):
        fig = time_series_visualizer.draw_box_plot()
        self.assertIsNotNone(fig)

if __name__ == "__main__":
    unittest.main()
