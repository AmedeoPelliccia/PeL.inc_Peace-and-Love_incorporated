import pytest

from sicoca import (
    CONTROLLED_ACRONYM,
    SICOCA,
    SicocaFramework,
    SicocaSemanticElement,
)


def test_sicoca_is_controlled_acronym():
    assert SICOCA.acronym == "SICO.CA"
    assert SICOCA.sico == "Sustainable Industrial Competitive Operations"
    assert SICOCA.ca == "Chained Algorithms"
    assert SICOCA.status == CONTROLLED_ACRONYM
    assert SICOCA.doctrine == "No more wars. Regeneration now."


def test_sustainability_is_authorization_condition():
    assert (
        SICOCA.exact_meaning
        == "Operaciones industriales competitivas que solo son admisibles si son sostenibles."
    )
    assert "condición de autorización" in SICOCA.sustainability_rule
    assert "etiqueta descriptiva" in SICOCA.sustainability_rule


@pytest.mark.parametrize(
    ("element", "label", "meaning"),
    [
        ("S", "Sustainable", "no externalización del daño hacia el más débil"),
        ("I", "Industrial", "producción de energía, materiales y sus logísticas"),
        (
            "C",
            "Competitive",
            "mejora sistémica sin guerras, muertes, heridos y destrucción",
        ),
        ("O", "Operations", "ejecución en tiempo casi real, no discurso"),
        (
            "CA",
            "Chained Algorithms",
            "algoritmos encadenados, auditables, gobernados y entonces extraíbles; minerías digitales las complicadas",
        ),
    ],
)
def test_semantic_expansion(element, label, meaning):
    expansion = SICOCA.expansion_for(element)
    assert expansion.label == label
    assert expansion.meaning == meaning


@pytest.mark.parametrize(
    ("element", "label"),
    [("s", "Sustainable"), ("ca", "Chained Algorithms")],
)
def test_semantic_expansion_lookup_is_case_insensitive(element, label):
    assert SICOCA.expansion_for(element).label == label


def test_formula_and_short_line_are_canonical():
    assert (
        SICOCA.formula
        == "SICO.CA = Sustainable Industrial Competitive Operations through Chained Algorithms"
    )
    assert (
        SICOCA.short_line
        == "SICO.CA: industry only if sustainable; competition not only if it is generative and regenerative, but: algorithms only if accountable."
    )


def test_unknown_semantic_element_is_rejected():
    with pytest.raises(KeyError):
        SICOCA.expansion_for("X")


def test_duplicate_semantic_elements_are_rejected():
    with pytest.raises(ValueError, match="duplicate semantic element: s"):
        SicocaFramework(
            acronym="TEST",
            sico="Test",
            ca="Chain",
            status=CONTROLLED_ACRONYM,
            doctrine="Doctrine",
            exact_meaning="Meaning",
            sustainability_rule="Rule",
            semantic_expansion=(
                SicocaSemanticElement("S", "Sustainable", "Meaning"),
                SicocaSemanticElement("s", "Duplicate sustainable", "Duplicate"),
            ),
            formula="Formula",
            short_line="Short line",
        )
