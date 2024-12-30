from pydantic import BaseModel
from typing import List, Optional


class RoeVWadeAnalysis(BaseModel):
    IsUnconstitutionalStatementPresent: bool
    OpinionType: Optional[str]  # Options: "Majority", "Dissenting", "Concurring"
    Excerpts: List[str]


class JudicialAuthorityAnalysis(BaseModel):
    IsExceedingAuthorityClaimPresent: bool
    OpinionType: Optional[str]  # Options: "Majority", "Dissenting", "Concurring"
    Excerpts: List[str]


class MoralEthicalOppositionAnalysis(BaseModel):
    IsMoralEthicalOppositionPresent: bool
    OpinionType: Optional[str]  # Options: "Majority", "Dissenting", "Concurring"
    Excerpts: List[str]


class LegislativeActionOrPolicyRecommendations(BaseModel):
    AreRecommendationsPresent: bool
    Excerpts: List[str]


class PublicOpinionConsideration(BaseModel):
    IsPublicOpinionConsidered: bool
    Excerpts: List[str]


class CaseAnalysis(BaseModel): # CLASS TO BE USED AS RESPONSE FORMAT
    CaseName: str
    DateOfDecision: str
    JudgesOnBench: List[str]
    RoeVWadeAnalysis: dict
    CitingRoeVWade: Optional[str]
    Opinions: dict
    LegislativeActionOrPolicyRecommendations: LegislativeActionOrPolicyRecommendations
    PublicOpinionConsideration: PublicOpinionConsideration


# Example instantiation:
case_analysis = CaseAnalysis(
    CaseName="Example v. State",
    DateOfDecision="2023-12-30",
    JudgesOnBench=["Judge A", "Judge B", "Judge C"],
    RoeVWadeAnalysis={
        "Constitutionality": RoeVWadeAnalysis(
            IsUnconstitutionalStatementPresent=True,
            OpinionType="Majority",
            Excerpts=[
                "Roe v. Wade overstepped the constitutional boundaries.",
                "The right to privacy does not explicitly guarantee abortion rights.",
            ],
        ),
        "JudicialAuthority": JudicialAuthorityAnalysis(
            IsExceedingAuthorityClaimPresent=False,
            OpinionType=None,
            Excerpts=[],
        ),
        "MoralEthicalOpposition": MoralEthicalOppositionAnalysis(
            IsMoralEthicalOppositionPresent=True,
            OpinionType="Dissenting",
            Excerpts=["Abortion conflicts with fundamental ethical principles."],
        ),
    },
    CitingRoeVWade="The case was cited to evaluate precedent regarding privacy rights.",
    Opinions={
        "MajorityOpinion": "The court ruled in favor of the respondent.",
        "DissentingOpinions": ["This decision undermines individual autonomy."],
        "ConcurringOpinions": ["The ruling aligns with constitutional principles."],
    },
    LegislativeActionOrPolicyRecommendations=LegislativeActionOrPolicyRecommendations(
        AreRecommendationsPresent=True,
        Excerpts=["The legislature should clarify abortion rights through explicit laws."],
    ),
    PublicOpinionConsideration=PublicOpinionConsideration(
        IsPublicOpinionConsidered=True,
        Excerpts=["The judgment aligns with prevailing public sentiment against abortion."],
    ),
)
