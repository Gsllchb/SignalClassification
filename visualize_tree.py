# coding: utf-8
import graphviz
from sklearn.externals import joblib
from sklearn.tree import export_graphviz

import dot
from constants import *

DECISION_TREE = joblib.load("Models/9223371868839381865.pkl")


def main():
    output_pdf(DECISION_TREE, ".temp")


def output_pdf(decision_tree, file: str) -> None:
    feature_names = (
        "layer",
        "left_time",
        "time",
        "right_time",
        "left_energy",
        "energy",
        "right_energy",
    )
    dot_data = export_graphviz(
        decision_tree,
        out_file=None,
        proportion=True,
        rounded=True,
        feature_names=feature_names,
    )
    graphviz.Source(dot_data).render(file, format="png")


if __name__ == '__main__':
    main()
