# sphinx/docutils API issue
# pyright: reportUnknownMemberType=false, reportUnknownVariableType=false
# pyright: reportUnknownArgumentType=false
from __future__ import annotations

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.application import Sphinx
from sphinx.writers.html5 import HTML5Translator


class exception_hierarchy(nodes.General, nodes.Element):
    pass


def visit_exception_hierarchy_node(self: HTML5Translator, node: exception_hierarchy):
    self.body.append(self.starttag(node, "div", CLASS="exception-hierarchy-content"))


def depart_exception_hierarchy_node(self: HTML5Translator, node: exception_hierarchy):
    self.body.append("</div>\n")


class ExceptionHierarchyDirective(Directive):
    has_content = True

    def run(self):
        self.assert_has_content()
        node = exception_hierarchy("\n".join(self.content))
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def setup(app: Sphinx):
    app.add_node(
        exception_hierarchy,
        html=(visit_exception_hierarchy_node, depart_exception_hierarchy_node),
    )
    app.add_directive("exception_hierarchy", ExceptionHierarchyDirective)