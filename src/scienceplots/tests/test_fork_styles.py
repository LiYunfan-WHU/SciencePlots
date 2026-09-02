"""Regression tests for styles maintained by the LiYunfan-WHU fork."""

import matplotlib as mpl
import matplotlib.pyplot as plt


def test_publication_style_contract():
    """Keep the reusable journal-figure defaults stable."""
    with plt.style.context(["science", "no-latex", "publication"]):
        assert mpl.rcParams["savefig.dpi"] == 600
        assert mpl.rcParams["font.size"] == 7
        assert mpl.rcParams["axes.labelpad"] == 4
        assert mpl.rcParams["lines.markersize"] == 4
        assert mpl.rcParams["xtick.major.size"] == 2.5
        assert mpl.rcParams["ytick.major.size"] == 2.5
        assert mpl.rcParams["xtick.major.pad"] == 3.5
        assert mpl.rcParams["ytick.major.pad"] == 3.5
        assert not mpl.rcParams["xtick.minor.visible"]
        assert not mpl.rcParams["ytick.minor.visible"]
        assert not mpl.rcParams["xtick.top"]
        assert not mpl.rcParams["ytick.right"]


def test_thesis_style_keeps_only_major_ticks():
    """Protect the latest local thesis tick policy."""
    with plt.style.context(["science", "no-latex", "thesis"]):
        assert mpl.rcParams["xtick.major.size"] == 3
        assert mpl.rcParams["ytick.major.size"] == 3
        assert not mpl.rcParams["xtick.minor.visible"]
        assert not mpl.rcParams["ytick.minor.visible"]
