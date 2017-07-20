# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import css as CSS
from chromewhip.protocol import dom as DOM
from chromewhip.protocol import page as Page

# DOMNode: A Node in the DOM tree.
class DOMNode(ChromeTypeBase):
    def __init__(self,
                 nodeType: Union['int'],
                 nodeName: Union['str'],
                 nodeValue: Union['str'],
                 backendNodeId: Union['DOM.BackendNodeId'],
                 textValue: Optional['str'] = None,
                 inputValue: Optional['str'] = None,
                 inputChecked: Optional['bool'] = None,
                 optionSelected: Optional['bool'] = None,
                 childNodeIndexes: Optional['[]'] = None,
                 attributes: Optional['[NameValue]'] = None,
                 pseudoElementIndexes: Optional['[]'] = None,
                 layoutNodeIndex: Optional['int'] = None,
                 documentURL: Optional['str'] = None,
                 baseURL: Optional['str'] = None,
                 contentLanguage: Optional['str'] = None,
                 publicId: Optional['str'] = None,
                 systemId: Optional['str'] = None,
                 frameId: Optional['Page.FrameId'] = None,
                 contentDocumentIndex: Optional['int'] = None,
                 importedDocumentIndex: Optional['int'] = None,
                 templateContentIndex: Optional['int'] = None,
                 pseudoType: Optional['DOM.PseudoType'] = None,
                 isClickable: Optional['bool'] = None,
                 ):

        self.nodeType = nodeType
        self.nodeName = nodeName
        self.nodeValue = nodeValue
        self.textValue = textValue
        self.inputValue = inputValue
        self.inputChecked = inputChecked
        self.optionSelected = optionSelected
        self.backendNodeId = backendNodeId
        self.childNodeIndexes = childNodeIndexes
        self.attributes = attributes
        self.pseudoElementIndexes = pseudoElementIndexes
        self.layoutNodeIndex = layoutNodeIndex
        self.documentURL = documentURL
        self.baseURL = baseURL
        self.contentLanguage = contentLanguage
        self.publicId = publicId
        self.systemId = systemId
        self.frameId = frameId
        self.contentDocumentIndex = contentDocumentIndex
        self.importedDocumentIndex = importedDocumentIndex
        self.templateContentIndex = templateContentIndex
        self.pseudoType = pseudoType
        self.isClickable = isClickable


# LayoutTreeNode: Details of an element in the DOM tree with a LayoutObject.
class LayoutTreeNode(ChromeTypeBase):
    def __init__(self,
                 domNodeIndex: Union['int'],
                 boundingBox: Union['DOM.Rect'],
                 layoutText: Optional['str'] = None,
                 inlineTextNodes: Optional['[CSS.InlineTextBox]'] = None,
                 styleIndex: Optional['int'] = None,
                 ):

        self.domNodeIndex = domNodeIndex
        self.boundingBox = boundingBox
        self.layoutText = layoutText
        self.inlineTextNodes = inlineTextNodes
        self.styleIndex = styleIndex


# ComputedStyle: A subset of the full ComputedStyle as defined by the request whitelist.
class ComputedStyle(ChromeTypeBase):
    def __init__(self,
                 properties: Union['[NameValue]'],
                 ):

        self.properties = properties


# NameValue: A name/value pair.
class NameValue(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 value: Union['str'],
                 ):

        self.name = name
        self.value = value


class DOMSnapshot(PayloadMixin):
    """ This domain facilitates obtaining document snapshots with DOM, layout, and style information.
    """
    @classmethod
    def getSnapshot(cls,
                    computedStyleWhitelist: Union['[]'],
                    ):
        """Returns a document snapshot, including the full DOM tree of the root node (including iframes, template contents, and imported documents) in a flattened array, as well as layout and white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is flattened. 
        :param computedStyleWhitelist: Whitelist of computed styles to return.
        :type computedStyleWhitelist: []
        """
        return (
            cls.build_send_payload("getSnapshot", {
                "computedStyleWhitelist": computedStyleWhitelist,
            }),
            cls.convert_payload({
                "domNodes": {
                    "class": [DOMNode],
                    "optional": False
                },
                "layoutTreeNodes": {
                    "class": [LayoutTreeNode],
                    "optional": False
                },
                "computedStyles": {
                    "class": [ComputedStyle],
                    "optional": False
                },
            })
        )

