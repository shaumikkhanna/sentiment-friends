from pydantic import BaseModel
from typing import List, Optional


class IsUnconstitutional(BaseModel):
    IsUnconstitutionalStatementPresent: bool
    OpinionType: Optional[str]  # Options: "Majority", "Dissenting", "Concurring"
    Excerpts: List[str]


class IsExceedingAuthority(BaseModel):
    IsExceedingAuthorityClaimPresent: bool
    OpinionType: Optional[str]  # Options: "Majority", "Dissenting", "Concurring"
    Excerpts: List[str]


class IsMoralEthicalOpposition(BaseModel):
    IsMoralEthicalOppositionPresent: bool
    OpinionType: Optional[str]  # Options: "Majority", "Dissenting", "Concurring"
    Excerpts: List[str]


class LegislativeActionRecommendations(BaseModel):
    AreRecommendationsPresent: bool
    Excerpts: List[str]


class PublicOpinionAnalysis(BaseModel):
    IsPublicOpinionMentioned: bool
    Excerpts: List[str]


class PrecedentReferences(BaseModel):
    AreOtherPrecedentsReferenced: bool
    Precedents: List[str]
    TreatmentOfRoe: Optional[str]  # e.g., "Affirmed", "Questioned", "Contradicted"


class RoeAuthorityAnalysis(BaseModel):
    IsRoeBindingPersuasiveQuestioned: bool
    OpinionType: Optional[str]  # Options: "Majority", "Dissenting", "Concurring"
    Excerpts: List[str]


class LegislativeDebatesAnalysis(BaseModel):
    AreDebatesMentioned: bool
    Excerpts: List[str]


class FutureOutlookAnalysis(BaseModel):
    IsFutureOutlookSuggested: bool
    Notes: Optional[str]


class CaseAnalysisSchema(BaseModel):
    CaseName: str
    DateOfDecision: str
    CourtJurisdiction: str  # e.g., Federal District Court, Circuit Court
    StateOrCircuit: str
    JudgesOnBench: List[str]
    Question6: IsUnconstitutional
    Question9: IsExceedingAuthority
    Question12: IsMoralEthicalOpposition
    ReasonForCitingRoe: Optional[str]
    SummaryOpinions: dict  # Format: {"Majority": str, "Dissenting": List[str], "Concurring": List[str]}
    LegislativeActionRecommendations: LegislativeActionRecommendations
    PublicOpinionAnalysis: PublicOpinionAnalysis
    PrecedentReferences: PrecedentReferences
    OutcomeOrHolding: str  # e.g., "Affirmed, reversed, remanded"
    RoeAuthorityAnalysis: RoeAuthorityAnalysis
    OtherConstitutionalGrounds: List[str]
    LegislativeDebatesAnalysis: LegislativeDebatesAnalysis
    FutureOutlook: FutureOutlookAnalysis
    AdditionalObservations: Optional[str]


# Example instantiation:
case_analysis = CaseAnalysisSchema(
    CaseName="Doe v. State",
    DateOfDecision="2024-12-30",
    CourtJurisdiction="Federal District Court",
    StateOrCircuit="5th Circuit",
    JudgesOnBench=["Judge A", "Judge B", "Judge C"],
    Question6=IsUnconstitutional(
        IsUnconstitutionalStatementPresent=True,
        OpinionType="Majority",
        Excerpts=["Roe v. Wade's basis in privacy rights is constitutionally unsound."],
    ),
    Question9=IsExceedingAuthority(
        IsExceedingAuthorityClaimPresent=False,
        OpinionType=None,
        Excerpts=[],
    ),
    Question12=IsMoralEthicalOpposition(
        IsMoralEthicalOppositionPresent=True,
        OpinionType="Dissenting",
        Excerpts=["Abortion conflicts with fundamental moral principles."],
    ),
    ReasonForCitingRoe="To evaluate the precedent's influence on privacy rights.",
    SummaryOpinions={
        "Majority": "The court upheld the lower court's ruling.",
        "Dissenting": ["The ruling undermines judicial consistency."],
        "Concurring": ["The decision aligns with historical interpretation."],
    },
    LegislativeActionRecommendations=LegislativeActionRecommendations(
        AreRecommendationsPresent=True,
        Excerpts=["The legislature should address abortion rights explicitly."],
    ),
    PublicOpinionAnalysis=PublicOpinionAnalysis(
        IsPublicOpinionMentioned=True,
        Excerpts=["Public sentiment on abortion heavily influenced the ruling."],
    ),
    PrecedentReferences=PrecedentReferences(
        AreOtherPrecedentsReferenced=True,
        Precedents=["Case A, Case B"],
        TreatmentOfRoe="Questioned",
    ),
    OutcomeOrHolding="Reversed. Citing Roe was central to the reversal.",
    RoeAuthorityAnalysis=RoeAuthorityAnalysis(
        IsRoeBindingPersuasiveQuestioned=True,
        OpinionType="Concurring",
        Excerpts=["Roe should be revisited to clarify its applicability."],
    ),
    OtherConstitutionalGrounds=["Fourteenth Amendment", "Privacy Rights"],
    LegislativeDebatesAnalysis=LegislativeDebatesAnalysis(
        AreDebatesMentioned=True,
        Excerpts=["The case references recent federal abortion debates."],
    ),
    FutureOutlook=FutureOutlookAnalysis(
        IsFutureOutlookSuggested=True,
        Notes="The court invited challenges to refine abortion jurisprudence."
    ),
    AdditionalObservations="The case marks a shift in how Roe is treated in lower courts."
)

print(case_analysis.json(indent=4))