import reflex as rx
from reflex.vars import Var
from typing import Any, Dict, List, Union
from reflex.vars.base import ImportVar, VarData

def cn(*args: Union[Var, str], **kwargs: Union[Var, str]) -> Var:
    """Merge Tailwind CSS classes."""
    processed_args: List[str] = [f"'{arg}'" if isinstance(arg, str) else str(arg) for arg in args]
    processed_kwargs: Dict[str, str] = {k: f"'{v}'" if isinstance(v, str) else str(v) for k, v in kwargs.items()}
    
    args_str: str = ", ".join(str(arg) for arg in processed_args)
    kwargs_str: str = ", ".join(f"{k}: {v}" for k, v in processed_kwargs.items())
    
    full_args: str = f"{args_str}{', ' if args_str and kwargs_str else ''}{kwargs_str}"
    
    return Var(
        f"cn({full_args})",
        _var_data=VarData(imports={"clsx-for-tailwind": ImportVar(tag="cn")}),
    )

class Accordion(rx.Component):
    """A vertically stacked set of interactive headings."""
    
    library: str = "@radix-ui/react-accordion"
    tag: str = "Root"
    
    is_collapsible: Var[bool]
    type: Var[str]

class AccordionItem(rx.Component):
    """An item within an Accordion."""
    
    library: str = "@radix-ui/react-accordion" 
    tag: str = "Item"

    style: Dict[str, Any] = {
        "border_bottom": "1px solid var(--border)",
    }

class AccordionTrigger(rx.Component):
    """The trigger button of an accordion item."""
    
    library: str = "@radix-ui/react-accordion"
    tag: str = "Trigger"
    
    style: Dict[str, Any] = {
        "display": "flex",
        "flex": 1,
        "align_items": "center", 
        "justify_content": "space_between",
        "padding_y": "4",
        "font_size": "sm",
        "font_medium": True,
        "transition": "all",
        "_hover": {
            "text_decoration": "underline"
        }
    }

class AccordionContent(rx.Component):
    """The content of an accordion item."""
    
    library: str = "@radix-ui/react-accordion"
    tag: str = "Content"
    
    style: Dict[str, Any] = {
        "overflow": "hidden",
        "font_size": "sm",
    }

# namings
accordion = Accordion.create
accordion_item = AccordionItem.create  
accordion_trigger = AccordionTrigger.create
accordion_content = AccordionContent.create
