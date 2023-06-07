from typing import List, Annotated
from .node import Node
from .link import Link
from .interaction import Interaction

DIAGRAM_TYPES = {
    "default": "graph",
    "flowchart": "flowchart"
}

DIAGRAM_ORIENTATION = {
    "default": "",
    "top to bottom": "TB",
    "top-down": "TD",
    "bottom to top": "BT",
    "right to left": "RL",
    "left to right": "LR",
}


class MermaidDiagram:
    def __init__(
        self,
        title: str = "",
        nodes: List[Node] = [],
        links: List[Link] = [],
        interactions: List[Interaction] = [],
        type="default",
        orientation="default",
            style_class_definitions=None 
    ):
        if style_class_definitions is None:
            style_class_definitions = {}
        self.style_class_definitions = style_class_definitions
        self.title = title
        self.nodes = nodes
        self.links = links
        self.interactions = interactions
        self.type = DIAGRAM_TYPES[type]
        self.orientation = DIAGRAM_ORIENTATION[orientation]

    def add_nodes(self, nodes=[]):
        self.nodes += nodes

    def add_links(self, links=[]):
        self.links += links

    def __str__(self):
        self.string = f"---\ntitle: {self.title}\n---\n"
        if self.style_class_definitions:
            style_class_string = '\n'.join([f'classDef {k} {v}' for k, v in self.style_class_definitions.items()]) + '\n'
        else:
            style_class_string = ''
        nodes_string = (
            '\n'.join([str(node) for node in self.nodes])
        )
        links_string = (
            '\n'.join([str(link) for link in self.links])
        )
        interactions_string = (
            '\n'.join([str(interaction) for interaction in self.interactions])
        )
        final_strings = list(
            filter(
                None,
                [
                    f"{self.type} {self.orientation}",
                    style_class_string,
                    nodes_string,
                    links_string,
                    interactions_string
                ]
            )
        )
        self.string += '\n'.join(final_strings)
        return self.string
