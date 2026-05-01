"""Ampel theoretical framework definitions for SICO.CA."""

from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Mapping


@dataclass(frozen=True)
class SicocaSemanticElement:
    element: str
    label: str
    meaning: str


@dataclass(frozen=True)
class SicocaFramework:
    acronym: str
    sico: str
    ca: str
    status: str
    doctrine: str
    exact_meaning: str
    sustainability_rule: str
    semantic_expansion: tuple[SicocaSemanticElement, ...]
    formula: str
    short_line: str
    _semantic_expansion_by_element: Mapping[str, SicocaSemanticElement] = field(
        init=False,
        repr=False,
    )

    def __post_init__(self) -> None:
        semantic_expansion_by_element: dict[str, SicocaSemanticElement] = {}
        for expansion in self.semantic_expansion:
            normalized = expansion.element.upper()
            if normalized in semantic_expansion_by_element:
                raise ValueError(f"duplicate semantic element: {expansion.element}")
            semantic_expansion_by_element[normalized] = expansion
        object.__setattr__(
            self,
            "_semantic_expansion_by_element",
            MappingProxyType(semantic_expansion_by_element),
        )

    def expansion_for(self, element: str) -> SicocaSemanticElement:
        normalized = element.upper()
        try:
            return self._semantic_expansion_by_element[normalized]
        except KeyError:
            raise KeyError(element) from None


CONTROLLED_ACRONYM = "controlled_acronym"

SICOCA = SicocaFramework(
    acronym="SICO.CA",
    sico="Sustainable Industrial Competitive Operations",
    ca="Chained Algorithms",
    status=CONTROLLED_ACRONYM,
    doctrine="No more wars. Regeneration now.",
    exact_meaning=(
        "Operaciones industriales competitivas que solo son admisibles si son sostenibles."
    ),
    sustainability_rule=(
        "La sostenibilidad no es una etiqueta descriptiva; es una condición de autorización."
    ),
    semantic_expansion=(
        SicocaSemanticElement(
            "S",
            "Sustainable",
            "no externalización del daño hacia el más débil",
        ),
        SicocaSemanticElement(
            "I",
            "Industrial",
            "producción de energía, materiales y sus logísticas",
        ),
        SicocaSemanticElement(
            "C",
            "Competitive",
            "mejora sistémica sin guerras, muertes, heridos y destrucción",
        ),
        SicocaSemanticElement(
            "O",
            "Operations",
            "ejecución en tiempo casi real, no discurso",
        ),
        SicocaSemanticElement(
            "CA",
            "Chained Algorithms",
            "algoritmos encadenados, auditables, gobernados y entonces extraíbles; minerías digitales las complicadas",
        ),
    ),
    formula=(
        "SICO.CA = Sustainable Industrial Competitive Operations "
        "through Chained Algorithms"
    ),
    short_line=(
        "SICO.CA: industry only if sustainable; competition not only if it is "
        "generative and regenerative, but: algorithms only if accountable."
    ),
)
