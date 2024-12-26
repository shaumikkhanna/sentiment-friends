from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "developer", 
            "content": """Context: We are social science researchers studying how Roe v. Wade has been cited across different courts, times, and jurisdictions. We seek detailed yet consistent information from each case.
Format Requirements:
Answer each question in a new line under the corresponding number (or letter) without repeating the question.
For yes/no questions, answer only “yes” or “no” (lowercase). If you cannot determine an answer, use “No information found.”
When providing quotes/excerpts, limit quotes to 3-5 lines each.
If the requested information is not found or not applicable, write “No information found.”
Level of Detail: Include exact names, brief excerpts from the decision, and label whether statements come from the majority, dissenting, or concurring opinions.
Model Note: Apply advanced reasoning to parse nuanced or implicit critiques of Roe v. Wade. If the text is ambiguous, provide your best interpretation.

Questions
Case Name
Date of Decision
Court/Jurisdiction
(e.g., Federal District Court, Circuit Court, State Supreme Court)
State or Circuit in which the case was decided
Full Names of the Judges on the Bench
If not all are listed, provide whatever names are given.
Yes or No: Are there any statements suggesting that Roe v. Wade was unconstitutional?
5a. If yes, specify majority, dissenting, or concurring.
5b. If yes, provide brief excerpts.
Yes or No: Does the opinion claim that Roe v. Wade exceeded judicial authority?
6a. If yes, specify majority, dissenting, or concurring.
6b. If yes, provide brief excerpts.
Yes or No: Are there any statements indicating moral or ethical opposition to abortion as a fundamental right?
7a. If yes, specify majority, dissenting, or concurring.
7b. If yes, provide brief excerpts.
Reason for citing Roe v. Wade
Why or how Roe is discussed.
Summary of Majority, Dissenting, and Concurring Opinions
Provide a concise description of each.
Yes or No: Were there any calls for legislative action or policy recommendations in the decision?
10a. If yes, provide brief excerpts or summaries.
Yes or No: Did the court mention or consider public opinion regarding abortion?
11a. If yes, provide brief excerpts.
Yes or No: Did the opinion reference other precedents related to abortion?
12a. If yes, how did the court treat Roe v. Wade in light of those precedents?
Outcome or Holding
What was the ultimate decision (e.g., affirmed, reversed, remanded)?
Did citing Roe have a direct influence on that outcome?
Yes or No: Was Roe v. Wade deemed binding, persuasive, or questioned authority?
14a. If yes, in which opinion (majority/dissenting/concurring) is this discussed?
14b. Provide brief excerpts if applicable.
References to Other Constitutional Grounds
If the case specifically cites other Amendments or legal doctrines alongside Roe (e.g., Fourteenth Amendment, privacy rights, due process), list them.
Yes or No: Does the case mention any state or federal legislative debates on abortion (e.g., mention of specific bills)?
18a. If yes, provide excerpts or summaries.
Future Outlook
Did the court suggest possible changes in abortion jurisprudence or invite future legal challenges?
Any Additional Observations
If there's anything else noteworthy about how Roe is treated, add a short note here.
Response Format:
Provide each answer on a new line, labeled with the corresponding question number or letter.
For yes/no questions, only answer “yes” or “no.”
For excerpt requests, provide short quotes (up to 3-5 lines).
If information is missing, write “No information found.”
"""
        },
        {
            "role": "user", 
            "content": """
<div>\n<center><b>505 U.S. 833 (1992)</b></center>\n<center>
        <h1>PLANNED PARENTHOOD OF SOUTHEASTERN PENNSYLVANIA et al.<br>\nv.<br>\nCASEY, GOVERNOR OF PENNSYLVANIA, et al.
        </h1>
    </center>\n<center>No. 91-744.</center>\n<center>
        <p><b>United States Supreme Court.</b></p>
    </center>\n<center>Argued April 22, 1992.</center>\n<center>Decided June 29, 1992.<sup>[*]</sup></center>
    \nCERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE THIRD CIRCUIT\n<p><span
            class=\"star-pagination\">*834</span> <span class=\"star-pagination\">*835</span> <span
            class=\"star-pagination\">*836</span> <span class=\"star-pagination\">*837</span> <span
            class=\"star-pagination\">*838</span> <span class=\"star-pagination\">*839</span> <span
            class=\"star-pagination\">*840</span> <span class=\"star-pagination\">*841</span> O'Connor, Kennedy, and
        Souter, JJ., announced the judgment of the Court and delivered the opinion of the Court with respect to Parts I,
        II, III, VA, VC, and VI, in which Blackmun and Stevens, JJ., joined, an opinion with respect to Part VE, in
        which Stevens, J., joined, and an opinion with respect to Parts IV, VB, and VD. Stevens, J., filed an opinion
        concurring in part and dissenting in part, <i>post,</i> p. 911. Blackmun, J., filed an opinion concurring in
        part, concurring in the judgment in part, and dissenting in part, <i>post,</i> p. 922. Rehnquist, C. J., filed
        an opinion concurring in the judgment in part and dissenting in part, in which <span
            class=\"star-pagination\">*842</span> White, Scalia, and Thomas, JJ., joined, <i>post,</i> p. 944. Scalia,
        J., filed an opinion concurring in the judgment in part and dissenting in part, in which Rehnquist, C. J., and
        White and Thomas, JJ., joined, <i>post,</i> p. 979.</p>\n<p><i>Kathryn Kolbert</i> argued the cause for
        petitioners in No. 91-744 and respondents in No. 91-902. With her on the briefs were <i>Janet Benshoof, Lynn M.
            Paltrow, Rachael N. Pine, Steven R. Shapiro, John A. Powell, Linda J. Wharton,</i> and <i>Carol E.
            Tracy.</i> </p>\n<p><i>Ernest D. Preate, Jr.,</i> Attorney General of Pennsylvania, argued the cause for
        respondents in No. 91-744 and petitioners in No. 91-902. With him on the brief were <i>John G. Knorr III,</i>
        Chief Deputy Attorney General, and <i>Kate L. Mershimer,</i> Senior Deputy Attorney General.</p>\n<p>
        <i>Solicitor General Starr</i> argued the cause for the United States as <i>amicus curiae</i> in support of
        respondents in No. 91-744 and petitioners in No. 91-902. With him on the brief were <i>Assistant Attorney
            General Gerson, Paul J. Larkin, Jr., Thomas G. Hungar,</i> and <i>Alfred R. Mollin.</i><sup>[]</sup>
    </p>\n
    <p><span class=\"star-pagination\">*843</span> Justice O'Connor, Justice Kennedy, and Justice Souter announced the
        judgment of the Court and delivered the opinion of the Court with respect to Parts I, II, III, VA, <span
            class=\"star-pagination\">*844</span> VC, and VI, an opinion with respect to Part VE, in which Justice
        Stevens joins, and an opinion with respect to Parts IV, VB, and VD.</p>\n<p></p>\n<h2>I</h2>\n<p>Liberty finds
        no refuge in a jurisprudence of doubt. Yet 19 years after our holding that the Constitution protects a woman's
        right to terminate her pregnancy in its early stages, <i>Roe</i> v. <i>Wade,</i> 410 U. S. 113 (1973), that
        definition of liberty is still questioned. Joining the respondents as <i>amicus curiae,</i> the United States,
        as it has done in five other cases in the last decade, again asks us to overrule <i>Roe.</i> See Brief for
        Respondents 104-117; Brief for United States as <i>Amicus Curiae</i> 8.</p>\n<p>At issue in these cases are five
        provisions of the Pennsylvania Abortion Control Act of 1982, as amended in 1988 and 1989. 18 Pa. Cons. Stat. §§
        3203-3220 (1990). Relevant portions of the Act are set forth in the Appendix. <i>Infra,</i> at 902. The Act
        requires that a woman seeking an abortion give her informed consent prior to the abortion procedure, and
        specifies that she be provided with certain information at least 24 hours before the abortion is performed. §
        3205. For a minor to obtain an abortion, the Act requires the informed consent of one of her parents, but
        provides for a judicial bypass option if the minor does not wish to or cannot obtain a parent's consent. § 3206.
        Another provision of the Act requires that, unless certain exceptions apply, a married woman seeking an abortion
        must sign a statement indicating that she has notified her husband of her intended abortion. § 3209. The Act
        exempts compliance with these three requirements in the event of a \"medical emergency,\" which is defined in §
        3203 of the Act. See §§ 3203, 3205(a), 3206(a), 3209(c). In addition to the above provisions regulating the
        performance of abortions, the Act imposes certain reporting requirements on facilities that provide abortion
        services. §§ 3207(b), 3214(a), 3214(f).</p>\n<p><span class=\"star-pagination\">*845</span> Before any of these
        provisions took effect, the petitioners, who are five abortion clinics and one physician representing himself as
        well as a class of physicians who provide abortion services, brought this suit seeking declaratory and
        injunctive relief. Each provision was challenged as unconstitutional on its face. The District Court entered a
        preliminary injunction against the enforcement of the regulations, and, after a 3-day bench trial, held all the
        provisions at issue here unconstitutional, entering a permanent injunction against Pennsylvania's enforcement of
        them. 744 F. Supp. 1323 (ED Pa. 1990). The Court of Appeals for the Third Circuit affirmed in part and reversed
        in part, upholding all of the regulations except for the husband notification requirement. 947 F. 2d 682 (1991).
        We granted certiorari. 502 U. S. 1056 (1992).</p>\n<p>The Court of Appeals found it necessary to follow an
        elaborate course of reasoning even to identify the first premise to use to determine whether the statute enacted
        by Pennsylvania meets constitutional standards. See 947 F. 2d, at 687 698. And at oral argument in this Court,
        the attorney for the parties challenging the statute took the position that none of the enactments can be upheld
        without overruling <i>Roe</i> v. <i>Wade</i><i>.</i> Tr. of Oral Arg. 5-6. We disagree with that analysis; but
        we acknowledge that our decisions after <i>Roe</i> cast doubt upon the meaning and reach of its holding.
        Further, The Chief Justice admits that he would overrule the central holding of<i>Roe</i> and adopt the rational
        relationship test as the sole criterion of constitutionality. See <i>post,</i> at 944, 966. State and federal
        courts as well as legislatures throughout the Union must have guidance as they seek to address this subject in
        conformance with the Constitution. Given these premises, we find it imperative to review once more the
        principles that define the rights of the woman and the legitimate authority of the State respecting the
        termination of pregnancies by abortion procedures.</p>\n<p>After considering the fundamental constitutional
        questions resolved by <i>Roe,</i> principles of institutional integrity, <span
            class=\"star-pagination\">*846</span> and the rule of <i>stare decisis,</i> we are led to conclude this: the
        essential holding of <i>Roe</i> v. <i>Wade</i> should be retained and once again reaffirmed.</p>\n<p>It must be
        stated at the outset and with clarity that <i>Roe</i> `s essential holding, the holding we reaffirm, has three
        parts. First is a recognition of the right of the woman to choose to have an abortion before viability and to
        obtain it without undue interference from the State. Before viability, the State's interests are not strong
        enough to support a prohibition of abortion or the imposition of a substantial obstacle to the woman's effective
        right to elect the procedure. Second is a confirmation of the State's power to restrict abortions after fetal
        viability, if the law contains exceptions for pregnancies which endanger the woman's life or health. And third
        is the principle that the State has legitimate interests from the outset of the pregnancy in protecting the
        health of the woman and the life of the fetus that may become a child. These principles do not contradict one
        another; and we adhere to each.</p>\n<p></p>\n<h2>II</h2>\n<p>Constitutional protection of the woman's decision
        to terminate her pregnancy derives from the Due Process Clause of the Fourteenth Amendment. It declares that no
        State shall \"deprive any person of life, liberty, or property, without due process of law.\" The controlling
        word in the cases before us is \"liberty.\" Although a literal reading of the Clause might suggest that it
        governs only the procedures by which a State may deprive persons of liberty, for at least 105 years, since
        <i>Mugler</i> v. <i>Kansas,</i> 123 U. S. 623, 660-661 (1887), the Clause has been understood to contain a
        substantive component as well, one \"barring certain government actions regardless of the fairness of the
        procedures used to implement them.\" <i>Daniels</i> v. <i>Williams,</i> 474 U. S. 327, 331 (1986). As Justice
        Brandeis (joined by Justice Holmes) observed, \"[d]espite arguments to the contrary which had seemed to me
        persuasive, it is settled that the due process clause of the Fourteenth <span
            class=\"star-pagination\">*847</span> Amendment applies to matters of substantive law as well as to matters
        of procedure. Thus all fundamental rights comprised within the term liberty are protected by the Federal
        Constitution from invasion by the States.\" <i>Whitney</i> v. <i>California,</i> 274 U. S. 357, 373 (1927)
        (concurring opinion). \"[T]he guaranties of due process, though having their roots in Magna Carta's <i>`per
            legem terrae'</i> and considered as procedural safeguards `against executive usurpation and tyranny,' have
        in this country `become bulwarks also against arbitrary legislation.' \" <i>Poe</i> v. <i>Ullman,</i> 367 U. S.
        497, 541 (1961) (Harlan, J., dissenting from dismissal on jurisdictional grounds) (quoting <i>Hurtado</i> v.
        <i>California,</i> 110 U. S. 516, 532 (1884)).
    </p>\n<p>The most familiar of the substantive liberties protected
        by the Fourteenth Amendment are those recognized by the Bill of Rights. We have held that the Due Process Clause
        of the Fourteenth Amendment incorporates most of the Bill of Rights against the States. See, <i>e. g.,
        </i><i>Duncan</i> v. <i>Louisiana,</i> 391 U. S. 145, 147-148 (1968). It is tempting, as a means of curbing the
        discretion of federal judges, to suppose that liberty encompasses no more than those rights already guaranteed
        to the individual against federal interference by the express provisions of the first eight Amendments to the
        Constitution. See <i>Adamson</i> v. <i>California,</i> 332 U. S. 46, 68-92 (1947) (Black, J., dissenting). But
        of course this Court has never accepted that view.</p>\n<p>It is also tempting, for the same reason, to suppose
        that the Due Process Clause protects only those practices, defined at the most specific level, that were
        protected against government interference by other rules of law when the Fourteenth Amendment was ratified. See
        <i>Michael H.</i> v. <i>Gerald D.,</i> 491 U. S. 110, 127-128, n. 6 (1989) (opinion of Scalia, J.). But such a
        view would be inconsistent with our law. It is a promise of the Constitution that there is a realm of personal
        liberty which the government may not enter. We have vindicated this principle before. Marriage is mentioned
        nowhere in the Bill of Rights and interracial marriage was illegal <span class=\"star-pagination\">*848</span>
        in most States in the 19th century, but the Court was no doubt correct in finding it to be an aspect of liberty
        protected against state interference by the substantive component of the Due Process Clause in <i>Loving</i> v.
        <i>Virginia,</i> 388 U. S. 1, 12 (1967) (relying, in an opinion for eight Justices, on the Due Process Clause).
        Similar examples may be found in <i>Turner</i> v. <i>Safley,</i> 482 U. S. 78, 94-99 (1987); in <i>Carey</i> v.
        <i>Population Services International,</i> 431 U. S. 678, 684-686 (1977); in <i>Griswold</i> v.
        <i>Connecticut,</i> 381 U. S. 479, 481-482 (1965), as well as in the separate opinions of a majority of the
        Members of the Court in that case, <i>id.,</i> at 486-488 (Goldberg, J., joined by Warren, C. J., and Brennan,
        J., concurring) (expressly relying on due process), <i>id.,</i> at 500-502 (Harlan, J., concurring in judgment)
        (same), <i>id.,</i> at 502-507 (White, J., concurring in judgment) (same); in <i>Pierce</i> v. <i>Society of
            Sisters,</i> 268 U. S. 510, 534-535 (1925); and in <i>Meyer</i> v. <i>Nebraska,</i> 262 U. S. 390, 399-403
        (1923).
    </p>\n<p>Neither the Bill of Rights nor the specific practices of States at the time of the adoption of
        the Fourteenth Amendment marks the outer limits of the substantive sphere of liberty which the Fourteenth
        Amendment protects. See U. S. Const., Amdt. 9. As the second Justice Harlan recognized:</p>\n<blockquote>\"[T]he
        full scope of the liberty guaranteed by the Due Process Clause cannot be found in or limited by the precise
        terms of the specific guarantees elsewhere provided in the Constitution. This `liberty' is not a series of
        isolated points pricked out in terms of the taking of property; the freedom of speech, press, and religion; the
        right to keep and bear arms; the freedom from unreasonable searches and seizures; and so on. It is a rational
        continuum which, broadly speaking, includes a freedom from all substantial arbitrary impositions and purposeless
        restraints, . . . and which also recognizes, what a reasonable and sensitive judgment must, that certain
        interests require particularly careful scrutiny of the state needs asserted to justify their abridgment.\"
        <i>Poe</i> v. <span class=\"star-pagination\">*849</span> <i>Ullman, supra,</i> at 543 (opinion dissenting from
        dismissal on jurisdictional grounds).
    </blockquote>\n<p>Justice Harlan wrote these words in addressing an issue
        the full Court did not reach in <i>Poe</i> v. <i>Ullman</i><i>,</i> but the Court adopted his position four
        Terms later in <i>Griswold</i> v. <i>Connecticut, supra</i><i>.</i> In <i>Griswold,</i> we held that the
        Constitution does not permit a State to forbid a married couple to use contraceptives. That same freedom was
        later guaranteed, under the Equal Protection Clause, for unmarried couples. See <i>Eisenstadt</i> v.
        <i>Baird,</i> 405 U. S. 438 (1972). Constitutional protection was extended to the sale and distribution of
        contraceptives in <i>Carey</i> v. <i>Population Services International, supra</i><i>.</i> It is settled now, as
        it was when the Court heard arguments in <i>Roe</i> v. <i>Wade</i><i>,</i> that the Constitution places limits
        on a State's right to interfere with a person's most basic decisions about family and parenthood, see
        <i>Carey</i> v. <i>Population Services International, supra</i><i>; </i><i>Moore</i> v. <i>East Cleveland,</i>
        431 U. S. 494 (1977); <i>Eisenstadt</i> v. <i>Baird, supra</i><i>; </i><i>Loving</i> v. <i>Virginia,
            supra</i><i>; </i><i>Griswold</i> v. <i>Connecticut, supra</i><i>; </i><i>Skinner</i> v. <i>Oklahoma ex rel.
            Williamson,</i> 316 U. S. 535 (1942); <i>Pierce</i> v. <i>Society of Sisters, supra</i><i>; </i><i>Meyer</i>
        v. <i>Nebraska, supra</i><i>,</i> as well as bodily integrity, see, <i>e. g., </i><i>Washington</i> v.
        <i>Harper,</i> 494 U. S. 210, 221-222 (1990); <i>Winston</i> v. <i>Lee,</i> 470 U. S. 753 (1985); <i>Rochin</i>
        v. <i>California,</i> 342 U. S. 165 (1952).
    </p>\n<p>The inescapable fact is that adjudication of substantive due
        process claims may call upon the Court in interpreting the Constitution to exercise that same capacity which by
        tradition courts always have exercised: reasoned judgment. Its boundaries are not susceptible of expression as a
        simple rule. That does not mean we are free to invalidate state policy choices with which we disagree; yet
        neither does it permit us to shrink from the duties of our office. As Justice Harlan observed:</p>\n<blockquote>
        \"Due process has not been reduced to any formula; its content cannot be determined by reference to any code.
    </blockquote>\n<blockquote>\n<span class=\"star-pagination\">*850</span> The best that can be said is that through
        the course of this Court's decisions it has represented the balance which our Nation, built upon postulates of
        respect for the liberty of the individual, has struck between that liberty and the demands of organized society.
        If the supplying of content to this Constitutional concept has of necessity been a rational process, it
        certainly has not been one where judges have felt free to roam where unguided speculation might take them. The
        balance of which I speak is the balance struck by this country, having regard to what history teaches are the
        traditions from which it developed as well as the traditions from which it broke. That tradition is a living
        thing. A decision of this Court which radically departs from it could not long survive, while a decision which
        builds on what has survived is likely to be sound. No formula could serve as a substitute, in this area, for
        judgment and restraint.\" <i>Poe</i> v. <i>Ullman,</i> 367 U. S., at 542 (opinion dissenting from dismissal on
        jurisdictional grounds).</blockquote>\n<p>See also <i>Rochin</i> v. <i>California, supra,</i> at 171-172
        (Frankfurter, J., writing for the Court) (\"To believe that this judicial exercise of judgment could be avoided
        by freezing `due process of law' at some fixed stage of time or thought is to suggest that the most important
        aspect of constitutional adjudication is a function for inanimate machines and not for judges\").</p>\n<p>Men
        and women of good conscience can disagree, and we suppose some always shall disagree, about the profound moral
        and spiritual implications of terminating a pregnancy, even in its earliest stage. Some of us as individuals
        find abortion offensive to our most basic principles of morality, but that cannot control our decision. Our
        obligation is to define the liberty of all, not to mandate our own moral code. The underlying constitutional
        issue is whether the State can resolve these philosophic questions in such a definitive way that a woman lacks
        all choice in the matter, except perhaps <span class=\"star-pagination\">*851</span> in those rare circumstances
        in which the pregnancy is itself a danger to her own life or health, or is the result of rape or incest.</p>\n
    <p>It is conventional constitutional doctrine that where reasonable people disagree the government can adopt one
        position or the other. See, <i>e. g., </i><i>Ferguson</i> v. <i>Skrupa,</i> 372 U. S. 726 (1963);
        <i>Williamson</i> v. <i>Lee Optical of Okla., Inc.,</i> 348 U. S. 483 (1955). That theorem, however, assumes a
        state of affairs in which the choice does not intrude upon a protected liberty. Thus, while some people might
        disagree about whether or not the flag should be saluted, or disagree about the proposition that it may not be
        defiled, we have ruled that a State may not compel or enforce one view or the other. See <i>West Virginia Bd. of
            Ed.</i> v. <i>Barnette,</i> 319 U. S. 624 (1943); <i>Texas</i> v. <i>Johnson,</i> 491 U. S. 397 (1989).
    </p>
    \n<p>Our law affords constitutional protection to personal decisions relating to marriage, procreation,
        contraception, family relationships, child rearing, and education. <i>Carey</i> v. <i>Population Services
            International,</i> 431 U. S., at 685. Our cases recognize \"the right of the <i>individual,</i> married or
        single, to be free from unwarranted governmental intrusion into matters so fundamentally affecting a person as
        the decision whether to bear or beget a child.\" <i>Eisenstadt</i> v. <i>Baird, supra,</i> at 453 (emphasis in
        original). Our precedents \"have respected the private realm of family life which the state cannot enter.\"
        <i>Prince</i> v. <i>Massachusetts,</i> 321 U. S. 158, 166 (1944). These matters, involving the most intimate and
        personal choices a person may make in a lifetime, choices central to personal dignity and autonomy, are central
        to the liberty protected by the Fourteenth Amendment. At the heart of liberty is the right to define one's own
        concept of existence, of meaning, of the universe, and of the mystery of human life. Beliefs about these matters
        could not define the attributes of personhood were they formed under compulsion of the State.
    </p>\n<p><span class=\"star-pagination\">*852</span> These considerations begin our analysis of the woman's interest
        in
        terminating her pregnancy but cannot end it, for this reason: though the abortion decision may originate within
        the zone of conscience and belief, it is more than a philosophic exercise. Abortion is a unique act. It is an
        act fraught with consequences for others: for the woman who must live with the implications of her decision; for
        the persons who perform and assist in the procedure; for the spouse, family, and society which must confront the
        knowledge that these procedures exist, procedures some deem nothing short of an act of violence against innocent
        human life; and, depending on one's beliefs, for the life or potential life that is aborted. Though abortion is
        conduct, it does not follow that the State is entitled to proscribe it in all instances. That is because the
        liberty of the woman is at stake in a sense unique to the human condition and so unique to the law. The mother
        who carries a child to full term is subject to anxieties, to physical constraints, to pain that only she must
        bear. That these sacrifices have from the beginning of the human race been endured by woman with a pride that
        ennobles her in the eyes of others and gives to the infant a bond of love cannot alone be grounds for the State
        to insist she make the sacrifice. Her suffering is too intimate and personal for the State to insist, without
        more, upon its own vision of the woman's role, however dominant that vision has been in the course of our
        history and our culture. The destiny of the woman must be shaped to a large extent on her own conception of her
        spiritual imperatives and her place in society.</p>\n<p>It should be recognized, moreover, that in some critical
        respects the abortion decision is of the same character as the decision to use contraception, to which
        <i>Griswold</i> v. <i>Connecticut</i><i>, </i><i>Eisenstadt</i> v. <i>Baird</i><i>,</i> and <i>Carey</i> v.
        <i>Population Services International</i> afford constitutional protection. We have no doubt as to the
        correctness of those decisions. They support <span class=\"star-pagination\">*853</span> the reasoning in
        <i>Roe</i> relating to the woman's liberty because they involve personal decisions concerning not only the
        meaning of procreation but also human responsibility and respect for it. As with abortion, reasonable people
        will have differences of opinion about these matters. One view is based on such reverence for the wonder of
        creation that any pregnancy ought to be welcomed and carried to full term no matter how difficult it will be to
        provide for the child and ensure its well-being. Another is that the inability to provide for the nurture and
        care of the infant is a cruelty to the child and an anguish to the parent. These are intimate views with
        infinite variations, and their deep, personal character underlay our decisions in <i>Griswold, Eisenstadt,</i>
        and <i>Carey.</i> The same concerns are present when the woman confronts the reality that, perhaps despite her
        attempts to avoid it, she has become pregnant.
    </p>\n<p>It was this dimension of personal liberty that <i>Roe</i>
        sought to protect, and its holding invoked the reasoning and the tradition of the precedents we have discussed,
        granting protection to substantive liberties of the person. <i>Roe</i> was, of course, an extension of those
        cases and, as the decision itself indicated, the separate States could act in some degree to further their own
        legitimate interests in protecting prenatal life. The extent to which the legislatures of the States might act
        to outweigh the interests of the woman in choosing to terminate her pregnancy was a subject of debate both in
        <i>Roe</i> itself and in decisions following it.
    </p>\n<p>While we appreciate the weight of the arguments made on
        behalf of the State in the cases before us, arguments which in their ultimate formulation conclude that
        <i>Roe</i> should be overruled, the reservations any of us may have in reaffirming the central holding of
        <i>Roe</i> are outweighed by the explication of individual liberty we have given combined with the force of
        <i>stare decisis.</i> We turn now to that doctrine.
    </p>\n<p></p>\n<h2>\n<span class=\"star-pagination\">*854</span> III</h2>\n<p></p>\n<h2>A</h2>\n<p>The obligation to
        follow precedent
        begins with necessity, and a contrary necessity marks its outer limit. With Cardozo, we recognize that no
        judicial system could do society's work if it eyed each issue afresh in every case that raised it. See B.
        Cardozo, The Nature of the Judicial Process 149 (1921). Indeed, the very concept of the rule of law underlying
        our own Constitution requires such continuity over time that a respect for precedent is, by definition,
        indispensable. See Powell, Stare Decisis and Judicial Restraint, 1991 Journal of Supreme Court History 13, 16.
        At the other extreme, a different necessity would make itself felt if a prior judicial ruling should come to be
        seen so clearly as error that its enforcement was for that very reason doomed.</p>\n<p>Even when the decision to
        overrule a prior case is not, as in the rare, latter instance, virtually foreordained, it is common wisdom that
        the rule of <i>stare decisis</i> is not an \"inexorable command,\" and certainly it is not such in every
        constitutional case, see <i>Burnet</i> v. <i>Coronado Oil &amp; Gas Co.,</i> 285 U. S. 393, 405-411 (1932)
        (Brandeis, J., dissenting). See also <i>Payne</i> v. <i>Tennessee,</i> 501 U. S. 808, 842 (1991) (Souter, J.,
        joined by Kennedy, J., concurring); <i>Arizona</i> v. <i>Rumsey,</i> 467 U. S. 203, 212 (1984). Rather, when
        this Court reexamines a prior holding, its judgment is customarily informed by a series of prudential and
        pragmatic considerations designed to test the consistency of overruling a prior decision with the ideal of the
        rule of law, and to gauge the respective costs of reaffirming and overruling a prior case. Thus, for example, we
        may ask whether the rule has proven to be intolerable simply in defying practical workability, <i>Swift &amp;
            Co.</i> v. <i>Wickham,</i> 382 U. S. 111, 116 (1965); whether the rule is subject to a kind of reliance that
        would lend a special hardship to the consequences of overruling and add inequity to the cost of repudiation,
        <i>e. g., </i><i>United States</i> v. <i>Title Ins. &amp; Trust</i> <span class=\"star-pagination\">*855</span>
        <i>Co.,</i> 265 U. S. 472, 486 (1924); whether related principles of law have so far developed as to have left
        the old rule no more than a remnant of abandoned doctrine, see <i>Patterson</i> v. <i>McLean Credit Union,</i>
        491 U. S. 164, 173-174 (1989); or whether facts have so changed, or come to be seen so differently, as to have
        robbed the old rule of significant application or justification, <i>e. g., </i><i>Burnet, supra,</i> at 412
        (Brandeis, J., dissenting).
    </p>\n<p>So in this case we may enquire whether <i>Roe</i> `s central rule has been
        found unworkable; whether the rule's limitation on state power could be removed without serious inequity to
        those who have relied upon it or significant damage to the stability of the society governed by it; whether the
        law's growth in the intervening years has left <i>Roe's</i> central rule a doctrinal anachronism discounted by
        society; and whether <i>Roe</i> `s premises of fact have so far changed in the ensuing two decades as to render
        its central holding somehow irrelevant or unjustifiable in dealing with the issue it addressed.</p>\n<p></p>\n
    <h2>1</h2>\n<p>Although <i>Roe</i> has engendered opposition, it has in no sense proven \"unworkable,\" see
        <i>Garcia</i> v. <i>San Antonio Metropolitan Transit Authority,</i> 469 U. S. 528, 546 (1985), representing as
        it does a simple limitation beyond which a state law is unenforceable. While <i>Roe</i> has, of course, required
        judicial assessment of state laws affecting the exercise of the choice guaranteed against government
        infringement, and although the need for such review will remain as a consequence of today's decision, the
        required determinations fall within judicial competence.
    </p>\n<p></p>\n<h2>2</h2>\n<p>The inquiry into reliance
        counts the cost of a rule's repudiation as it would fall on those who have relied reasonably on the rule's
        continued application. Since the classic case for weighing reliance heavily in favor of following the earlier
        rule occurs in the commercial context, see <i>Payne</i> v. <i>Tennes-</i> <span
            class=\"star-pagination\">*856</span> <i>see, supra,</i> at 828, where advance planning of great precision
        is most obviously a necessity, it is no cause for surprise that some would find no reliance worthy of
        consideration in support of <i>Roe.</i> </p>\n<p>While neither respondents nor their <i>amici</i> in so many
        words deny that the abortion right invites some reliance prior to its actual exercise, one can readily imagine
        an argument stressing the dissimilarity of this case to one involving property or contract. Abortion is
        customarily chosen as an unplanned response to the consequence of unplanned activity or to the failure of
        conventional birth control, and except on the assumption that no intercourse would have occurred but for
        <i>Roe</i> `s holding, such behavior may appear to justify no reliance claim. Even if reliance could be claimed
        on that unrealistic assumption, the argument might run, any reliance interest would be <i>de minimis.</i> This
        argument would be premised on the hypothesis that reproductive planning could take virtually immediate account
        of any sudden restoration of state authority to ban abortions.
    </p>\n<p>To eliminate the issue of reliance that
        easily, however, one would need to limit cognizable reliance to specific instances of sexual activity. But to do
        this would be simply to refuse to face the fact that for two decades of economic and social developments, people
        have organized intimate relationships and made choices that define their views of themselves and their places in
        society, in reliance on the availability of abortion in the event that contraception should fail. The ability of
        women to participate equally in the economic and social life of the Nation has been facilitated by their ability
        to control their reproductive lives. See, <i>e. g.,</i> R. Petchesky, Abortion and Woman's Choice 109, 133, n. 7
        (rev. ed. 1990). The Constitution serves human values, and while the effect of reliance on <i>Roe</i> cannot be
        exactly measured, neither can the certain cost of overruling <i>Roe</i> for people who have ordered their
        thinking and living around that case be dismissed.</p>\n<p></p>\n<h2>\n<span
            class=\"star-pagination\">*857</span> 3</h2>\n<p>No evolution of legal principle has left <i>Roe</i> `s
        doctrinal footings weaker than they were in 1973. No development of constitutional law since the case was
        decided has implicitly or explicitly left <i>Roe</i> behind as a mere survivor of obsolete constitutional
        thinking.</p>\n<p>It will be recognized, of course, that <i>Roe</i> stands at an intersection of two lines of
        decisions, but in whichever doctrinal category one reads the case, the result for present purposes will be the
        same. The <i>Roe</i> Court itself placed its holding in the succession of cases most prominently exemplified by
        <i>Griswold</i> v. <i>Connecticut,</i> 381 U. S. 479 (1965). See <i>Roe,</i> 410 U. S., at 152-153. When it is
        so seen, <i>Roe</i> is clearly in no jeopardy, since subsequent constitutional developments have neither
        disturbed, nor do they threaten to diminish, the scope of recognized protection accorded to the liberty relating
        to intimate relationships, the family, and decisions about whether or not to beget or bear a child. See, <i>e.
            g., </i><i>Carey</i> v. <i>Population Services International,</i> 431 U. S. 678 (1977); <i>Moore</i> v.
        <i>East Cleveland,</i> 431 U. S. 494 (1977).
    </p>\n<p><i>Roe,</i> however, may be seen not only as an exemplar of
        <i>Griswold</i> liberty but as a rule (whether or not mistaken) of personal autonomy and bodily integrity, with
        doctrinal affinity to cases recognizing limits on governmental power to mandate medical treatment or to bar its
        rejection. If so, our cases since <i>Roe</i> accord with <i>Roe</i> `s view that a State's interest in the
        protection of life falls short of justifying any plenary override of individual liberty claims. <i>Cruzan</i> v.
        <i>Director, Mo. Dept. of Health,</i> 497 U. S. 261, 278 (1990); cf., <i>e. g., </i><i>Riggins</i> v.
        <i>Nevada,</i> 504 U. S. 127, 135 (1992); <i>Washington</i> v. <i>Harper,</i> 494 U. S. 210 (1990); see also,
        <i>e. g., </i><i>Rochin</i> v. <i>California,</i> 342 U. S. 165 (1952); <i>Jacobson</i> v. <i>Massachusetts,</i>
        197 U. S. 11, 24-30 (1905).
    </p>\n<p>Finally, one could classify <i>Roe</i> as <i>sui generis.</i> If the case is
        so viewed, then there clearly has been no erosion of its central determination. The original holding resting on
        the <span class=\"star-pagination\">*858</span> concurrence of seven Members of the Court in 1973 was expressly
        affirmed by a majority of six in 1983, see <i>Akron</i> v. <i>Akron Center for Reproductive Health, Inc.,</i>
        462 U. S. 416 <i>(Akron I)</i><i>,</i> and by a majority of five in 1986, see <i>Thornburgh</i> v. <i>American
            College of Obstetricians and Gynecologists,</i> 476 U. S. 747, expressing adherence to the constitutional
        ruling despite legislative efforts in some States to test its limits. More recently, in <i>Webster</i> v.
        <i>Reproductive Health Services,</i> 492 U. S. 490 (1989), although two of the present authors questioned the
        trimester framework in a way consistent with our judgment today, see <i>id.,</i> at 518 (Rehnquist, C. J.,
        joined by White and Kennedy, JJ.); <i>id.,</i> at 529 (O'Connor, J., concurring in part and concurring in
        judgment), a majority of the Court either decided to reaffirm or declined to address the constitutional validity
        of the central holding of <i>Roe.</i> See <i>Webster,</i> 492 U. S., at 521 (Rehnquist, C. J., joined by White
        and Kennedy, JJ.); <i>id.,</i> at 525-526 (O'Connor, J., concurring in part and concurring in judgment);
        <i>id.,</i> at 537, 553 (Blackmun, J., joined by Brennan and Marshall, JJ., concurring in part and dissenting in
        part); <i>id.,</i> at 561-563 (Stevens, J., concurring in part and dissenting in part).
    </p>\n<p>Nor will courts
        building upon <i>Roe</i> be likely to hand down erroneous decisions as a consequence. Even on the assumption
        that the central holding of <i>Roe</i> was in error, that error would go only to the strength of the state
        interest in fetal protection, not to the recognition afforded by the Constitution to the woman's liberty. The
        latter aspect of the decision fits comfortably within the framework of the Court's prior decisions, including
        <i>Skinner</i> v. <i>Oklahoma ex rel. Williamson,</i> 316 U. S. 535 (1942); <i>Griswold, supra; Loving</i> v.
        <i>Virginia,</i> 388 U. S. 1 (1967); and <i>Eisenstadt</i> v. <i>Baird,</i> 405 U. S. 438 (1972), the holdings
        of which are \"not a series of isolated points,\" but mark a \"rational continuum.\" <i>Poe</i> v.
        <i>Ullman,</i> 367 U. S., at 543 (Harlan, J., dissenting). As we described in <span
            class=\"star-pagination\">*859</span> <i>Carey</i> v. <i>Population Services International,
            supra</i><i>,</i> the liberty which encompasses those decisions
    </p>\n<blockquote>\"includes `the interest in
        independence in making certain kinds of important decisions.' While the outer limits of this aspect of
        [protected liberty] have not been marked by the Court, it is clear that among the decisions that an individual
        may make without unjustified government interference are personal decisions `relating to marriage, procreation,
        contraception, family relationships, and child rearing and education.' \" 431 U. S., at 684-685 (citations
        omitted).</blockquote>\n<p>The soundness of this prong of the <i>Roe</i> analysis is apparent from a
        consideration of the alternative. If indeed the woman's interest in deciding whether to bear and beget a child
        had not been recognized as in <i>Roe,</i> the State might as readily restrict a woman's right to choose to carry
        a pregnancy to term as to terminate it, to further asserted state interests in population control, or eugenics,
        for example. Yet <i>Roe</i> has been sensibly relied upon to counter any such suggestions. <i>E. g.,
        </i><i>Arnold</i> v. <i>Board of Education of Escambia County, Ala.,</i> 880 F. 2d 305, 311 (CA11 1989) (relying
        upon <i>Roe</i> and concluding that government officials violate the Constitution by coercing a minor to have an
        abortion); <i>Avery</i> v. <i>County of Burke,</i> 660 F. 2d 111, 115 (CA4 1981) (county agency inducing teenage
        girl to undergo unwanted sterilization on the basis of misrepresentation that she had sickle cell trait); see
        also <i>In re Quinlan,</i> 70 N. J. 10, 355 A. 2d 647 (relying on <i>Roe</i> in finding a right to terminate
        medical treatment), cert. denied <i>sub nom. </i><i>Garger</i> v. <i>New Jersey,</i> 429 U. S. 922 (1976)). In
        any event, because <i>Roe</i> `s scope is confined by the fact of its concern with postconception potential
        life, a concern otherwise likely to be implicated only by some forms of contraception protected independently
        under <i>Griswold</i> and later cases, any error in <i>Roe</i> is unlikely to have serious ramifications in
        future cases.</p>\n<p></p>\n<h2>\n<span class=\"star-pagination\">*860</span> 4</h2>\n<p>We have seen how time
        has overtaken some of <i>Roe</i> `s factual assumptions: advances in maternal health care allow for abortions
        safe to the mother later in pregnancy than was true in 1973, see <i>Akron I, supra,</i> at 429, n. 11, and
        advances in neonatal care have advanced viability to a point somewhat earlier. Compare <i>Roe,</i> 410 U. S., at
        160, with <i>Webster, supra,</i> at 515-516 (opinion of Rehnquist, C. J.); see <i>Akron I,</i> 462 U. S., at
        457, and n. 5 (O'Connor, J., dissenting). But these facts go only to the scheme of time limits on the
        realization of competing interests, and the divergences from the factual premises of 1973 have no bearing on the
        validity of <i>Roe</i> `s central holding, that viability marks the earliest point at which the State's interest
        in fetal life is constitutionally adequate to justify a legislative ban on nontherapeutic abortions. The
        soundness or unsoundness of that constitutional judgment in no sense turns on whether viability occurs at
        approximately 28 weeks, as was usual at the time of <i>Roe,</i> at 23 to 24 weeks, as it sometimes does today,
        or at some moment even slightly earlier in pregnancy, as it may if fetal respiratory capacity can somehow be
        enhanced in the future. Whenever it may occur, the attainment of viability may continue to serve as the critical
        fact, just as it has done since <i>Roe</i> was decided; which is to say that no change in <i>Roe</i> `s factual
        underpinning has left its central holding obsolete, and none supports an argument for overruling it.</p>\n<p>
    </p>\n<h2>5</h2>\n<p>The sum of the precedential enquiry to this point shows <i>Roe</i> `s underpinnings unweakened
        in any way affecting its central holding. While it has engendered disapproval, it has not been unworkable. An
        entire generation has come of age free to assume <i>Roe</i> `s concept of liberty in defining the capacity of
        women to act in society, and to make reproductive decisions; no erosion of principle going to liberty or
        personal autonomy has left <i>Roe</i> `s central holding a doctrinal remnant; <span
            class=\"star-pagination\">*861</span> <i>Roe</i> portends no developments at odds with other precedent for
        the analysis of personal liberty; and no changes of fact have rendered viability more or less appropriate as the
        point at which the balance of interests tips. Within the bounds of normal <i>stare decisis</i> analysis, then,
        and subject to the considerations on which it customarily turns, the stronger argument is for affirming
        <i>Roe</i> `s central holding, with whatever degree of personal reluctance any of us may have, not for
        overruling it.
    </p>\n<p></p>\n<h2>B</h2>\n<p>In a less significant case, <i>stare decisis</i> analysis could, and
        would, stop at the point we have reached. But the sustained and widespread debate <i>Roe</i> has provoked calls
        for some comparison between that case and others of comparable dimension that have responded to national
        controversies and taken on the impress of the controversies addressed. Only two such decisional lines from the
        past century present themselves for examination, and in each instance the result reached by the Court accorded
        with the principles we apply today.</p>\n<p>The first example is that line of cases identified with
        <i>Lochner</i> v. <i>New York,</i> 198 U. S. 45 (1905), which imposed substantive limitations on legislation
        limiting economic autonomy in favor of health and welfare regulation, adopting, in Justice Holmes's view, the
        theory of laissez-faire. <i>Id.,</i> at 75 (dissenting opinion). The <i>Lochner</i> decisions were exemplified
        by <i>Adkins</i> v. <i>Children's Hospital of District of Columbia,</i> 261 U. S. 525 (1923), in which this
        Court held it to be an infringement of constitutionally protected liberty of contract to require the employers
        of adult women to satisfy minimum wage standards. Fourteen years later, <i>West Coast Hotel Co.</i> v.
        <i>Parrish,</i> 300 U. S. 379 (1937), signaled the demise of <i>Lochner</i> by overruling <i>Adkins.</i> In the
        meantime, the Depression had come and, with it, the lesson that seemed unmistakable to most people by 1937, that
        the interpretation of contractual freedom protected in <i>Adkins</i> rested on fundamentally <span
            class=\"star-pagination\">*862</span> false factual assumptions about the capacity of a relatively
        unregulated market to satisfy minimal levels of human welfare. See <i>West Coast Hotel Co., supra,</i> at 399.
        As Justice Jackson wrote of the constitutional crisis of 1937 shortly before he came on the bench: \"The older
        world of <i>laissez faire</i> was recognized everywhere outside the Court to be dead.\" The Struggle for
        Judicial Supremacy 85 (1941). The facts upon which the earlier case had premised a constitutional resolution of
        social controversy had proven to be untrue, and history's demonstration of their untruth not only justified but
        required the new choice of constitutional principle that <i>West Coast Hotel</i> announced. Of course, it was
        true that the Court lost something by its misperception, or its lack of prescience, and the Court-packing crisis
        only magnified the loss; but the clear demonstration that the facts of economic life were different from those
        previously assumed warranted the repudiation of the old law.
    </p>\n<p>The second comparison that 20th century
        history invites is with the cases employing the separate-but-equal rule for applying the Fourteenth Amendment's
        equal protection guarantee. They began with <i>Plessy</i> v. <i>Ferguson,</i> 163 U. S. 537 (1896), holding that
        legislatively mandated racial segregation in public transportation works no denial of equal protection,
        rejecting the argument that racial separation enforced by the legal machinery of American society treats the
        black race as inferior. The <i>Plessy</i> Court considered \"the underlying fallacy of the plaintiff's argument
        to consist in the assumption that the enforced separation of the two races stamps the colored race with a badge
        of inferiority. If this be so, it is not by reason of anything found in the act, but solely because the colored
        race chooses to put that construction upon it.\" <i>Id.,</i> at 551. Whether, as a matter of historical fact,
        the Justices in the <i>Plessy</i> majority believed this or not, see <i>id.,</i> at 557, 562 (Harlan, J.,
        dissenting), this understanding of the implication of segregation was the stated justification for the Court's
        opinion. But this understanding of <span class=\"star-pagination\">*863</span> the facts and the rule it was
        stated to justify were repudiated in <i>Brown</i> v. <i>Board of Education,</i> 347 U. S. 483 (1954) <i>(Brown
            I)</i><i>.</i> As one commentator observed, the question before the Court in <i>Brown</i> was \"whether
        discrimination inheres in that segregation which is imposed by law in the twentieth century in certain specific
        states in the American Union. And that question has meaning and can find an answer only on the ground of history
        and of common knowledge about the facts of life in the times and places aforesaid.\" Black, The Lawfulness of
        the Segregation Decisions, 69 Yale L. J. 421, 427 (1960).</p>\n<p>The Court in <i>Brown</i> addressed these
        facts of life by observing that whatever may have been the understanding in <i>Plessy</i> `s time of the power
        of segregation to stigmatize those who were segregated with a \"badge of inferiority,\" it was clear by 1954
        that legally sanctioned segregation had just such an effect, to the point that racially separate public
        educational facilities were deemed inherently unequal. 347 U. S., at 494-495. Society's understanding of the
        facts upon which a constitutional ruling was sought in 1954 was thus fundamentally different from the basis
        claimed for the decision in 1896. While we think <i>Plessy</i> was wrong the day it was decided, see <i>Plessy,
            supra,</i> at 552-564 (Harlan, J., dissenting), we must also recognize that the <i>Plessy</i> Court's
        explanation for its decision was so clearly at odds with the facts apparent to the Court in 1954 that the
        decision to reexamine <i>Plessy</i> was on this ground alone not only justified but required.</p>\n<p><i>West
            Coast Hotel</i> and <i>Brown</i> each rested on facts, or an understanding of facts, changed from those
        which furnished the claimed justifications for the earlier constitutional resolutions. Each case was
        comprehensible as the Court's response to facts that the country could understand, or had come to understand
        already, but which the Court of an earlier day, as its own declarations disclosed, had not been able to
        perceive. As the decisions were thus comprehensible <span class=\"star-pagination\">*864</span> they were also
        defensible, not merely as the victories of one doctrinal school over another by dint of numbers (victories
        though they were), but as applications of constitutional principle to facts as they had not been seen by the
        Court before. In constitutional adjudication as elsewhere in life, changed circumstances may impose new
        obligations, and the thoughtful part of the Nation could accept each decision to overrule a prior case as a
        response to the Court's constitutional duty.</p>\n<p>Because the cases before us present no such occasion it
        could be seen as no such response. Because neither the factual underpinnings of <i>Roe</i> `s central holding
        nor our understanding of it has changed (and because no other indication of weakened precedent has been shown),
        the Court could not pretend to be reexamining the prior law with any justification beyond a present doctrinal
        disposition to come out differently from the Court of 1973. To overrule prior law for no other reason than that
        would run counter to the view repeated in our cases, that a decision to overrule should rest on some special
        reason over and above the belief that a prior case was wrongly decided. See<i>, e. g., </i><i>Mitchell</i> v.
        <i>W. T. Grant Co.,</i> 416 U. S. 600, 636 (1974) (Stewart, J., dissenting) (\"A basic change in the law upon a
        ground no firmer than a change in our membership invites the popular misconception that this institution is
        little different from the two political branches of the Government. No misconception could do more lasting
        injury to this Court and to the system of law which it is our abiding mission to serve\"); <i>Mapp</i> v.
        <i>Ohio,</i> 367 U. S. 643, 677 (1961) (Harlan, J., dissenting).
    </p>\n<p></p>\n<h2>C</h2>\n<p>The examination of
        the conditions justifying the repudiation of <i>Adkins</i> by <i>West Coast Hotel</i> and <i>Plessy</i> by
        <i>Brown</i> is enough to suggest the terrible price that would have been paid if the Court had not overruled as
        it did. In the present cases, however, as our analysis to this point makes clear, the terrible price would be
        paid for overruling. Our analysis <span class=\"star-pagination\">*865</span> would not be complete, however,
        without explaining why overruling <i>Roe</i> `s central holding would not only reach an unjustifiable result
        under principles of <i>stare decisis,</i> but would seriously weaken the Court's capacity to exercise the
        judicial power and to function as the Supreme Court of a Nation dedicated to the rule of law. To understand why
        this would be so it is necessary to understand the source of this Court's authority, the conditions necessary
        for its preservation, and its relationship to the country's understanding of itself as a constitutional
        Republic.
    </p>\n<p>The root of American governmental power is revealed most clearly in the instance of the power
        conferred by the Constitution upon the Judiciary of the United States and specifically upon this Court. As
        Americans of each succeeding generation are rightly told, the Court cannot buy support for its decisions by
        spending money and, except to a minor degree, it cannot independently coerce obedience to its decrees. The
        Court's power lies, rather, in its legitimacy, a product of substance and perception that shows itself in the
        people's acceptance of the Judiciary as fit to determine what the Nation's law means and to declare what it
        demands.</p>\n<p>The underlying substance of this legitimacy is of course the warrant for the Court's decisions
        in the Constitution and the lesser sources of legal principle on which the Court draws. That substance is
        expressed in the Court's opinions, and our contemporary understanding is such that a decision without principled
        justification would be no judicial act at all. But even when justification is furnished by apposite legal
        principle, something more is required. Because not every conscientious claim of principled justification will be
        accepted as such, the justification claimed must be beyond dispute. The Court must take care to speak and act in
        ways that allow people to accept its decisions on the terms the Court claims for them, as grounded truly in
        principle, not as compromises with social and political pressures having, as such, no bearing on the principled
        choices that the Court is <span class=\"star-pagination\">*866</span> obliged to make. Thus, the Court's
        legitimacy depends on making legally principled decisions under circumstances in which their principled
        character is sufficiently plausible to be accepted by the Nation.</p>\n<p>The need for principled action to be
        perceived as such is implicated to some degree whenever this, or any other appellate court, overrules a prior
        case. This is not to say, of course, that this Court cannot give a perfectly satisfactory explanation in most
        cases. People understand that some of the Constitution's language is hard to fathom and that the Court's
        Justices are sometimes able to perceive significant facts or to understand principles of law that eluded their
        predecessors and that justify departures from existing decisions. However upsetting it may be to those most
        directly affected when one judicially derived rule replaces another, the country can accept some correction of
        error without necessarily questioning the legitimacy of the Court.</p>\n<p>In two circumstances, however, the
        Court would almost certainly fail to receive the benefit of the doubt in overruling prior cases. There is,
        first, a point beyond which frequent overruling would overtax the country's belief in the Court's good faith.
        Despite the variety of reasons that may inform and justify a decision to overrule, we cannot forget that such a
        decision is usually perceived (and perceived correctly) as, at the least, a statement that a prior decision was
        wrong. There is a limit to the amount of error that can plausibly be imputed to prior Courts. If that limit
        should be exceeded, disturbance of prior rulings would be taken as evidence that justifiable reexamination of
        principle had given way to drives for particular results in the short term. The legitimacy of the Court would
        fade with the frequency of its vacillation.</p>\n<p>That first circumstance can be described as hypothetical;
        the second is to the point here and now. Where, in the performance of its judicial duties, the Court decides a
        case in such a way as to resolve the sort of intensely divisive controversy reflected in <i>Roe</i> and those
        rare, comparable cases, its <span class=\"star-pagination\">*867</span> decision has a dimension that the
        resolution of the normal case does not carry. It is the dimension present whenever the Court's interpretation of
        the Constitution calls the contending sides of a national controversy to end their national division by
        accepting a common mandate rooted in the Constitution.</p>\n<p>The Court is not asked to do this very often,
        having thus addressed the Nation only twice in our lifetime, in the decisions of <i>Brown</i> and <i>Roe.</i>
        But when the Court does act in this way, its decision requires an equally rare precedential force to counter the
        inevitable efforts to overturn it and to thwart its implementation. Some of those efforts may be mere
        unprincipled emotional reactions; others may proceed from principles worthy of profound respect. But whatever
        the premises of opposition may be, only the most convincing justification under accepted standards of precedent
        could suffice to demonstrate that a later decision overruling the first was anything but a surrender to
        political pressure, and an unjustified repudiation of the principle on which the Court staked its authority in
        the first instance. So to overrule under fire in the absence of the most compelling reason to reexamine a
        watershed decision would subvert the Court's legitimacy beyond any serious question. Cf. <i>Brown</i> v.
        <i>Board of Education,</i> 349 U. S. 294, 300 (1955) <i>(Brown II)</i> (\"[I]t should go without saying that the
        vitality of th[e] constitutional principles [announced in <i>Brown I,</i> ] cannot be allowed to yield simply
        because of disagreement with them\").
    </p>\n<p>The country's loss of confidence in the Judiciary would be
        underscored by an equally certain and equally reasonable condemnation for another failing in overruling
        unnecessarily and under pressure. Some cost will be paid by anyone who approves or implements a constitutional
        decision where it is unpopular, or who refuses to work to undermine the decision or to force its reversal. The
        price may be criticism or ostracism, or it may be violence. An extra price will be paid by those who themselves
        disapprove of the decision's results <span class=\"star-pagination\">*868</span> when viewed outside of
        constitutional terms, but who nevertheless struggle to accept it, because they respect the rule of law. To all
        those who will be so tested by following, the Court implicitly undertakes to remain steadfast, lest in the end a
        price be paid for nothing. The promise of constancy, once given, binds its maker for as long as the power to
        stand by the decision survives and the understanding of the issue has not changed so fundamentally as to render
        the commitment obsolete. From the obligation of this promise this Court cannot and should not assume any
        exemption when duty requires it to decide a case in conformance with the Constitution. A willing breach of it
        would be nothing less than a breach of faith, and no Court that broke its faith with the people could sensibly
        expect credit for principle in the decision by which it did that.</p>\n<p>It is true that diminished legitimacy
        may be restored, but only slowly. Unlike the political branches, a Court thus weakened could not seek to regain
        its position with a new mandate from the voters, and even if the Court could somehow go to the polls, the loss
        of its principled character could not be retrieved by the casting of so many votes. Like the character of an
        individual, the legitimacy of the Court must be earned over time. So, indeed, must be the character of a Nation
        of people who aspire to live according to the rule of law. Their belief in themselves as such a people is not
        readily separable from their understanding of the Court invested with the authority to decide their
        constitutional cases and speak before all others for their constitutional ideals. If the Court's legitimacy
        should be undermined, then, so would the country be in its very ability to see itself through its constitutional
        ideals. The Court's concern with legitimacy is not for the sake of the Court, but for the sake of the Nation to
        which it is responsible.</p>\n<p>The Court's duty in the present cases is clear. In 1973, it confronted the
        already-divisive issue of governmental power <span class=\"star-pagination\">*869</span> to limit personal
        choice to undergo abortion, for which it provided a new resolution based on the due process guaranteed by the
        Fourteenth Amendment. Whether or not a new social consensus is developing on that issue, its divisiveness is no
        less today than in 1973, and pressure to overrule the decision, like pressure to retain it, has grown only more
        intense. A decision to overrule <i>Roe</i> `s essential holding under the existing circumstances would address
        error, if error there was, at the cost of both profound and unnecessary damage to the Court's legitimacy, and to
        the Nation's commitment to the rule of law. It is therefore imperative to adhere to the essence of <i>Roe</i> `s
        original decision, and we do so today.</p>\n<p></p>\n<h2>IV</h2>\n<p>From what we have said so far it follows
        that it is a constitutional liberty of the woman to have some freedom to terminate her pregnancy. We conclude
        that the basic decision in <i>Roe</i> was based on a constitutional analysis which we cannot now repudiate. The
        woman's liberty is not so unlimited, however, that from the outset the State cannot show its concern for the
        life of the unborn, and at a later point in fetal development the State's interest in life has sufficient force
        so that the right of the woman to terminate the pregnancy can be restricted.</p>\n<p>That brings us, of course,
        to the point where much criticism has been directed at <i>Roe,</i> a criticism that always inheres when the
        Court draws a specific rule from what in the Constitution is but a general standard. We conclude, however, that
        the urgent claims of the woman to retain the ultimate control over her destiny and her body, claims implicit in
        the meaning of liberty, require us to perform that function. Liberty must not be extinguished for want of a line
        that is clear. And it falls to us to give some real substance to the woman's liberty to determine whether to
        carry her pregnancy to full term.</p>\n<p><span class=\"star-pagination\">*870</span> We conclude the line
        should be drawn at viability, so that before that time the woman has a right to choose to terminate her
        pregnancy. We adhere to this principle for two reasons. First, as we have said, is the doctrine of <i>stare
            decisis.</i> Any judicial act of line-drawing may seem somewhat arbitrary, but <i>Roe</i> was a reasoned
        statement, elaborated with great care. We have twice reaffirmed it in the face of great opposition. See
        <i>Thornburgh</i> v. <i>American College of Obstetricians and Gynecologists,</i> 476 U. S., at 759; <i>Akron
            I</i> , 462 U. S., at 419-420. Although we must overrule those parts of <i>Thornburgh</i> and <i>Akron I</i>
        which, in our view, are inconsistent with <i>Roe</i> `s statement that the State has a legitimate interest in
        promoting the life or potential life of the unborn, see <i>infra,</i> at 882-883, the central premise of those
        cases represents an unbroken commitment by this Court to the essential holding of <i>Roe.</i> It is that premise
        which we reaffirm today.
    </p>\n<p>The second reason is that the concept of viability, as we noted in <i>Roe,</i>
        is the time at which there is a realistic possibility of maintaining and nourishing a life outside the womb, so
        that the independent existence of the second life can in reason and all fairness be the object of state
        protection that now overrides the rights of the woman. See <i>Roe</i> v. <i>Wade,</i> 410 U. S., at 163.
        Consistent with other constitutional norms, legislatures may draw lines which appear arbitrary without the
        necessity of offering a justification. But courts may not. We must justify the lines we draw. And there is no
        line other than viability which is more workable. To be sure, as we have said, there may be some medical
        developments that affect the precise point of viability, see <i>supra,</i> at 860, but this is an imprecision
        within tolerable limits given that the medical community and all those who must apply its discoveries will
        continue to explore the matter. The viability line also has, as a practical matter, an element of fairness. In
        some broad sense it might be said that a woman who fails to act before viability has consented to the State's
        intervention on behalf of the developing child.</p>\n<p><span class=\"star-pagination\">*871</span> The woman's
        right to terminate her pregnancy before viability is the most central principle of <i>Roe</i> v.
        <i>Wade</i><i>.</i> It is a rule of law and a component of liberty we cannot renounce.
    </p>\n<p>On the other side
        of the equation is the interest of the State in the protection of potential life. The <i>Roe</i> Court
        recognized the State's \"important and legitimate interest in protecting the potentiality of human life.\"
        <i>Roe, supra,</i> at 162. The weight to be given this state interest, not the strength of the woman's interest,
        was the difficult question faced in <i>Roe.</i> We do not need to say whether each of us, had we been Members of
        the Court when the valuation of the state interest came before it as an original matter, would have concluded,
        as the <i>Roe</i> Court did, that its weight is insufficient to justify a ban on abortions prior to viability
        even when it is subject to certain exceptions. The matter is not before us in the first instance, and coming as
        it does after nearly 20 years of litigation in <i>Roe</i> `s wake we are satisfied that the immediate question
        is not the soundness of <i>Roe</i> `s resolution of the issue, but the precedential force that must be accorded
        to its holding. And we have concluded that the essential holding of <i>Roe</i> should be reaffirmed.
    </p>\n<p>Yet
        it must be remembered that <i>Roe</i> v. <i>Wade</i> speaks with clarity in establishing not only the woman's
        liberty but also the State's \"important and legitimate interest in potential life.\" <i>Roe, supra,</i> at 163.
        That portion of the decision in <i>Roe</i> has been given too little acknowledgment and implementation by the
        Court in its subsequent cases. Those cases decided that any regulation touching upon the abortion decision must
        survive strict scrutiny, to be sustained only if drawn in narrow terms to further a compelling state interest.
        See, <i>e. g., </i><i>Akron I, supra,</i> at 427. Not all of the cases decided under that formulation can be
        reconciled with the holding in <i>Roe</i> itself that the State has legitimate interests in the health of the
        woman and in protecting the potential life within her. In resolving this tension, we choose to rely upon
        <i>Roe,</i> as against the later cases.
    </p>\n<p><span class=\"star-pagination\">*872</span> <i>Roe</i>
        established a trimester framework to govern abortion regulations. Under this elaborate but rigid construct,
        almost no regulation at all is permitted during the first trimester of pregnancy; regulations designed to
        protect the woman's health, but not to further the State's interest in potential life, are permitted during the
        second trimester; and during the third trimester, when the fetus is viable, prohibitions are permitted provided
        the life or health of the mother is not at stake. <i>Roe, supra,</i> at 163-166. Most of our cases since
        <i>Roe</i> have involved the application of rules derived from the trimester framework. See, <i>e. g.,
        </i><i>Thornburgh</i> v. <i>American College of Obstetricians and Gynecologists, supra</i><i>; </i><i>Akron I,
            supra</i><i>.</i>
    </p>\n<p>The trimester framework no doubt was erected to ensure that the woman's right to
        choose not become so subordinate to the State's interest in promoting fetal life that her choice exists in
        theory but not in fact. We do not agree, however, that the trimester approach is necessary to accomplish this
        objective. A framework of this rigidity was unnecessary and in its later interpretation sometimes contradicted
        the State's permissible exercise of its powers.</p>\n<p>Though the woman has a right to choose to terminate or
        continue her pregnancy before viability, it does not at all follow that the State is prohibited from taking
        steps to ensure that this choice is thoughtful and informed. Even in the earliest stages of pregnancy, the State
        may enact rules and regulations designed to encourage her to know that there are philosophic and social
        arguments of great weight that can be brought to bear in favor of continuing the pregnancy to full term and that
        there are procedures and institutions to allow adoption of unwanted children as well as a certain degree of
        state assistance if the mother chooses to raise the child herself. \"`[T]he Constitution does not forbid a State
        or city, pursuant to democratic processes, from expressing a preference for normal childbirth.' \"
        <i>Webster</i> v. <i>Reproductive Health Services,</i> 492 U. S., at 511 (opinion of <span
            class=\"star-pagination\">*873</span> the Court) (quoting <i>Poelker</i> v. <i>Doe,</i> 432 U. S. 519, 521
        (1977)). It follows that States are free to enact laws to provide a reasonable framework for a woman to make a
        decision that has such profound and lasting meaning. This, too, we find consistent with <i>Roe</i> `s central
        premises, and indeed the inevitable consequence of our holding that the State has an interest in protecting the
        life of the unborn.
    </p>\n<p>We reject the trimester framework, which we do not consider to be part of the
        essential holding of <i>Roe.</i> See <i>Webster</i> v. <i>Reproductive Health Services,</i> 492 U. S., at 518
        (opinion of Rehnquist, C. J.); <i>id.,</i> at 529 (O'Connor, J., concurring in part and concurring in judgment)
        (describing the trimester framework as \"problematic\"). Measures aimed at ensuring that a woman's choice
        contemplates the consequences for the fetus do not necessarily interfere with the right recognized in
        <i>Roe,</i> although those measures have been found to be inconsistent with the rigid trimester framework
        announced in that case. A logical reading of the central holding in <i>Roe</i> itself, and a necessary
        reconciliation of the liberty of the woman and the interest of the State in promoting prenatal life, require, in
        our view, that we abandon the trimester framework as a rigid prohibition on all previability regulation aimed at
        the protection of fetal life. The trimester framework suffers from these basic flaws: in its formulation it
        misconceives the nature of the pregnant woman's interest; and in practice it undervalues the State's interest in
        potential life, as recognized in <i>Roe.</i>
    </p>\n<p>As our jurisprudence relating to all liberties save
        perhaps abortion has recognized, not every law which makes a right more difficult to exercise is, <i>ipso
            facto,</i> an infringement of that right. An example clarifies the point. We have held that not every ballot
        access limitation amounts to an infringement of the right to vote. Rather, the States are granted substantial
        flexibility in establishing the framework within which voters choose the candidates for whom they <span
            class=\"star-pagination\">*874</span> wish to vote. <i>Anderson</i> v. <i>Celebrezze,</i> 460 U. S. 780, 788
        (1983); <i>Norman</i> v. <i>Reed,</i> 502 U. S. 279 (1992).</p>\n<p>The abortion right is similar. Numerous
        forms of state regulation might have the incidental effect of increasing the cost or decreasing the availability
        of medical care, whether for abortion or any other medical procedure. The fact that a law which serves a valid
        purpose, one not designed to strike at the right itself, has the incidental effect of making it more difficult
        or more expensive to procure an abortion cannot be enough to invalidate it. Only where state regulation imposes
        an undue burden on a woman's ability to make this decision does the power of the State reach into the heart of
        the liberty protected by the Due Process Clause. See <i>Hodgson</i> v. <i>Minnesota,</i> 497 U. S. 417, 458-459
        (1990) (O'Connor, J., concurring in part and concurring in judgment in part); <i>Ohio</i> v. <i>Akron Center for
            Reproductive Health,</i> 497 U. S. 502, 519-520 (1990) <i>(Akron II)</i> (opinion of Kennedy, J.);
        <i>Webster</i> v. <i>Reproductive Health Services, supra,</i> at 530 (O'Connor, J., concurring in part and
        concurring in judgment); <i>Thornburgh</i> v. <i>American College of Obstetricians and Gynecologists,</i> 476 U.
        S., at 828 (O'Connor, J., dissenting); <i>Simopoulos</i> v. <i>Virginia,</i> 462 U. S. 506, 520 (1983)
        (O'Connor, J., concurring in part and concurring in judgment); <i>Planned Parenthood Assn. of Kansas City, Mo.,
            Inc.</i> v. <i>Ashcroft,</i> 462 U. S. 476, 505 (1983) (O'Connor, J., concurring in judgment in part and
        dissenting in part); <i>Akron I,</i> 462 U. S., at 464 (O'Connor, J., joined by White and Rehnquist, JJ.,
        dissenting); <i>Bellotti</i> v. <i>Baird,</i> 428 U. S. 132, 147 (1976) <i>(Bellotti I)</i> .
    </p>\n<p>For the
        most part, the Court's early abortion cases adhered to this view. In <i>Maher</i> v. <i>Roe,</i> 432 U. S. 464,
        473-474 (1977), the Court explained: \"<i>Roe</i> did not declare an unqualified `constitutional right to an
        abortion,' as the District Court seemed to think. Rather, the right protects the woman from unduly burdensome
        interference with her freedom to decide whether to terminate her pregnancy.\" See <span
            class=\"star-pagination\">*875</span> also <i>Doe</i> v. <i>Bolton,</i> 410 U. S. 179, 198 (1973) (\"[T]he
        interposition of the hospital abortion committee is unduly restrictive of the patient's rights\"); <i>Bellotti
            I, supra,</i> at 147 (State may not \"impose undue burdens upon a minor capable of giving an informed
        consent\"); <i>Harris</i> v. <i>McRae,</i> 448 U. S. 297, 314 (1980) (citing <i>Maher, supra</i> ). Cf.
        <i>Carey</i> v. <i>Population Services International,</i> 431 U. S., at 688 (\"[T]he same test must be applied
        to state regulations that burden an individual's right to decide to prevent conception or terminate pregnancy by
        substantially limiting access to the means of effectuating that decision as is applied to state statutes that
        prohibit the decision entirely\").
    </p>\n<p>These considerations of the nature of the abortion right illustrate
        that it is an overstatement to describe it as a right to decide whether to have an abortion \"without
        interference from the State.\" <i>Planned Parenthood of Central Mo.</i> v. <i>Danforth,</i> 428 U. S. 52, 61
        (1976). All abortion regulations interfere to some degree with a woman's ability to decide whether to terminate
        her pregnancy. It is, as a consequence, not surprising that despite the protestations contained in the original
        <i>Roe</i> opinion to the effect that the Court was not recognizing an absolute right, 410 U. S., at 154-155,
        the Court's experience applying the trimester framework has led to the striking down of some abortion
        regulations which in no real sense deprived women of the ultimate decision. Those decisions went too far because
        the right recognized by <i>Roe</i> is a right \"to be free from unwarranted governmental intrusion into matters
        so fundamentally affecting a person as the decision whether to bear or beget a child.\" <i>Eisenstadt</i> v.
        <i>Baird,</i> 405 U. S., at 453. Not all governmental intrusion is of necessity unwarranted; and that brings us
        to the other basic flaw in the trimester framework: even in <i>Roe</i> `s terms, in practice it undervalues the
        State's interest in the potential life within the woman.
    </p>\n<p><i>Roe</i> v. <i>Wade</i> was express in its
        recognition of the State's \"important and legitimate interest[s] in preserving and protecting <span
            class=\"star-pagination\">*876</span> the health of the pregnant woman [and] in protecting the potentiality
        of human life.\" 410 U. S., at 162. The trimester framework, however, does not fulfill <i>Roe</i> `s own promise
        that the State has an interest in protecting fetal life or potential life. <i>Roe</i> began the contradiction by
        using the trimester framework to forbid any regulation of abortion designed to advance that interest before
        viability. <i>Id.,</i> at 163. Before viability, <i>Roe</i> and subsequent cases treat all governmental attempts
        to influence a woman's decision on behalf of the potential life within her as unwarranted. This treatment is, in
        our judgment, incompatible with the recognition that there is a substantial state interest in potential life
        throughout pregnancy. Cf. <i>Webster,</i> 492 U. S., at 519 (opinion of Rehnquist, C. J.); <i>Akron I,
            supra,</i> at 461 (O'Connor, J., dissenting).</p>\n<p>The very notion that the State has a substantial
        interest in potential life leads to the conclusion that not all regulations must be deemed unwarranted. Not all
        burdens on the right to decide whether to terminate a pregnancy will be undue. In our view, the undue burden
        standard is the appropriate means of reconciling the State's interest with the woman's constitutionally
        protected liberty.</p>\n<p>The concept of an undue burden has been utilized by the Court as well as individual
        Members of the Court, including two of us, in ways that could be considered inconsistent. See, <i>e. g.,
        </i><i>Hodgson</i> v. <i>Minnesota, supra,</i> at 459-461 (O'Connor, J., concurring in part and concurring in
        judgment); <i>Akron II, supra,</i> at 519-520 (opinion of Kennedy, J.); <i>Thornburgh</i> v. <i>American College
            of Obstetricians and Gynecologists, supra,</i> at 828-829 (O'Connor, J., dissenting); <i>Akron I, supra,</i>
        at 461-466 (O'Connor, J., dissenting); <i>Harris</i> v. <i>McRae, supra,</i> at 314; <i>Maher</i> v. <i>Roe,
            supra,</i> at 473; <i>Beal</i> v. <i>Doe,</i> 432 U. S. 438, 446 (1977); <i>Bellotti I, supra,</i> at 147.
        Because we set forth a standard of general application to which we intend to adhere, it is important to clarify
        what is meant by an undue burden.</p>\n<p><span class=\"star-pagination\">*877</span> A finding of an undue
        burden is a shorthand for the conclusion that a state regulation has the purpose or effect of placing a
        substantial obstacle in the path of a woman seeking an abortion of a nonviable fetus. A statute with this
        purpose is invalid because the means chosen by the State to further the interest in potential life must be
        calculated to inform the woman's free choice, not hinder it. And a statute which, while furthering the interest
        in potential life or some other valid state interest, has the effect of placing a substantial obstacle in the
        path of a woman's choice cannot be considered a permissible means of serving its legitimate ends. To the extent
        that the opinions of the Court or of individual Justices use the undue burden standard in a manner that is
        inconsistent with this analysis, we set out what in our view should be the controlling standard. Cf.
        <i>McCleskey</i> v. <i>Zant,</i> 499 U. S. 467, 489 (1991) (attempting \"to define the doctrine of abuse of the
        writ with more precision\" after acknowledging tension among earlier cases). In our considered judgment, an
        undue burden is an unconstitutional burden. See <i>Akron II,</i> 497 U. S., at 519-520 (opinion of Kennedy, J.).
        Understood another way, we answer the question, left open in previous opinions discussing the undue burden
        formulation, whether a law designed to further the State's interest in fetal life which imposes an undue burden
        on the woman's decision before fetal viability could be constitutional. See, <i>e. g., </i><i>Akron I,</i> 462
        U. S., at 462-463 (O'Connor, J., dissenting). The answer is no.
    </p>\n<p>Some guiding principles should emerge.
        What is at stake is the woman's right to make the ultimate decision, not a right to be insulated from all others
        in doing so. Regulations which do no more than create a structural mechanism by which the State, or the parent
        or guardian of a minor, may express profound respect for the life of the unborn are permitted, if they are not a
        substantial obstacle to the woman's exercise of the right to choose. See <i>infra,</i> at 899-900 (addressing
        Pennsylvania's parental consent requirement).</p>\n<p><span class=\"star-pagination\">*878</span> Unless it has
        that effect on her right of choice, a state measure designed to persuade her to choose childbirth over abortion
        will be upheld if reasonably related to that goal. Regulations designed to foster the health of a woman seeking
        an abortion are valid if they do not constitute an undue burden.</p>\n<p>Even when jurists reason from shared
        premises, some disagreement is inevitable. Compare <i>Hodgson,</i> 497 U. S., at 482-497 (Kennedy, J.,
        concurring in judgment in part and dissenting in part), with <i>id.,</i> at 458-460 (O'Connor, J., concurring in
        part and concurring in judgment in part). That is to be expected in the application of any legal standard which
        must accommodate life's complexity. We do not expect it to be otherwise with respect to the undue burden
        standard. We give this summary:</p>\n<p>(a) To protect the central right recognized by <i>Roe</i> v. <i>Wade</i>
        while at the same time accommodating the State's profound interest in potential life, we will employ the undue
        burden analysis as explained in this opinion. An undue burden exists, and therefore a provision of law is
        invalid, if its purpose or effect is to place a substantial obstacle in the path of a woman seeking an abortion
        before the fetus attains viability.</p>\n<p>(b) We reject the rigid trimester framework of <i>Roe</i> v.
        <i>Wade</i><i>.</i> To promote the State's profound interest in potential life, throughout pregnancy the State
        may take measures to ensure that the woman's choice is informed, and measures designed to advance this interest
        will not be invalidated as long as their purpose is to persuade the woman to choose childbirth over abortion.
        These measures must not be an undue burden on the right.
    </p>\n<p>(c) As with any medical procedure, the State
        may enact regulations to further the health or safety of a woman seeking an abortion. Unnecessary health
        regulations that have the purpose or effect of presenting a substantial obstacle to a woman seeking an abortion
        impose an undue burden on the right.</p>\n<p><span class=\"star-pagination\">*879</span> (d) Our adoption of the
        undue burden analysis does not disturb the central holding of <i>Roe</i> v. <i>Wade</i><i>,</i> and we reaffirm
        that holding. Regardless of whether exceptions are made for particular circumstances, a State may not prohibit
        any woman from making the ultimate decision to terminate her pregnancy before viability.</p>\n<p>(e) We also
        reaffirm <i>Roe</i> `s holding that \"subsequent to viability, the State in promoting its interest in the
        potentiality of human life may, if it chooses, regulate, and even proscribe, abortion except where it is
        necessary, in appropriate medical judgment, for the preservation of the life or health of the mother.\"
        <i>Roe</i> v. <i>Wade,</i> 410 U. S., at 164-165.
    </p>\n<p>These principles control our assessment of the
        Pennsylvania statute, and we now turn to the issue of the validity of its challenged provisions.</p>\n<p></p>\n
    <h2>V</h2>\n<p>The Court of Appeals applied what it believed to be the undue burden standard and upheld each of the
        provisions except for the husband notification requirement. We agree generally with this conclusion, but refine
        the undue burden analysis in accordance with the principles articulated above. We now consider the separate
        statutory sections at issue.</p>\n<p></p>\n<h2>A</h2>\n<p>Because it is central to the operation of various
        other requirements, we begin with the statute's definition of medical emergency. Under the statute, a medical
        emergency is</p>\n<blockquote>\"[t]hat condition which, on the basis of the physician's good faith clinical
        judgment, so complicates the medical condition of a pregnant woman as to necessitate the immediate abortion of
        her pregnancy to avert her death or for which a delay will create serious risk of substantial and irreversible
        impairment of a major bodily function.\" 18 Pa. Cons. Stat. § 3203 (1990).</blockquote>\n<p><span
            class=\"star-pagination\">*880</span> Petitioners argue that the definition is too narrow, contending that
        it forecloses the possibility of an immediate abortion despite some significant health risks. If the contention
        were correct, we would be required to invalidate the restrictive operation of the provision, for the essential
        holding of <i>Roe</i> forbids a State to interfere with a woman's choice to undergo an abortion procedure if
        continuing her pregnancy would constitute a threat to her health. 410 U. S., at 164. See also <i>Harris</i> v.
        <i>McRae,</i> 448 U. S., at 316.
    </p>\n<p>The District Court found that there were three serious conditions which
        would not be covered by the statute: preeclampsia, inevitable abortion, and premature ruptured membrane. 744 F.
        Supp., at 1378. Yet, as the Court of Appeals observed, 947 F. 2d, at 700-701, it is undisputed that under some
        circumstances each of these conditions could lead to an illness with substantial and irreversible consequences.
        While the definition could be interpreted in an unconstitutional manner, the Court of Appeals construed the
        phrase \"serious risk\" to include those circumstances. <i>Id.,</i> at 701. It stated: \"[W]e read the medical
        emergency exception as intended by the Pennsylvania legislature to assure that compliance with its abortion
        regulations would not in any way pose a significant threat to the life or health of a woman.\" <i>Ibid.</i> As
        we said in <i>Brockett</i> v. <i>Spokane Arcades, Inc.,</i> 472 U. S. 491, 499-500 (1985): \"Normally, . . . we
        defer to the construction of a state statute given it by the lower federal courts.\" Indeed, we have said that
        we will defer to lower court interpretations of state law unless they amount to \"plain\" error. <i>Palmer</i>
        v. <i>Hoffman,</i> 318 U. S. 109, 118 (1943). This \"`reflect[s] our belief that district courts and courts of
        appeals are better schooled in and more able to interpret the laws of their respective States.' \" <i>Frisby</i>
        v. <i>Schultz,</i> 487 U. S. 474, 482 (1988) (citation omitted). We adhere to that course today, and conclude
        that, as construed by the Court of Appeals, the medical emergency definition imposes no undue burden on a
        woman's abortion right.</p>\n<p></p>\n<h2>\n<span class=\"star-pagination\">*881</span> B</h2>\n<p>We next
        consider the informed consent requirement. 18 Pa. Cons. Stat. § 3205 (1990). Except in a medical emergency, the
        statute requires that at least 24 hours before performing an abortion a physician inform the woman of the nature
        of the procedure, the health risks of the abortion and of childbirth, and the \"probable gestational age of the
        unborn child.\" The physician or a qualified nonphysician must inform the woman of the availability of printed
        materials published by the State describing the fetus and providing information about medical assistance for
        childbirth, information about child support from the father, and a list of agencies which provide adoption and
        other services as alternatives to abortion. An abortion may not be performed unless the woman certifies in
        writing that she has been informed of the availability of these printed materials and has been provided them if
        she chooses to view them.</p>\n<p>Our prior decisions establish that as with any medical procedure, the State
        may require a woman to give her written informed consent to an abortion. See <i>Planned Parenthood of Central
            Mo.</i> v. <i>Danforth,</i> 428 U. S., at 67. In this respect, the statute is unexceptional. Petitioners
        challenge the statute's definition of informed consent because it includes the provision of specific information
        by the doctor and the mandatory 24-hour waiting period. The conclusions reached by a majority of the Justices in
        the separate opinions filed today and the undue burden standard adopted in this opinion require us to overrule
        in part some of the Court's past decisions, decisions driven by the trimester framework's prohibition of all
        previability regulations designed to further the State's interest in fetal life.</p>\n<p>In <i>Akron I,</i> 462
        U. S. 416 (1983), we invalidated an ordinance which required that a woman seeking an abortion be provided by her
        physician with specific information \"designed to influence the woman's informed choice between abortion or
        childbirth.\" <i>Id.,</i> at 444. As we later described <span class=\"star-pagination\">*882</span> the <i>Akron
            I</i> holding in <i>Thornburgh</i> v. <i>American College of Obstetricians and Gynecologists,</i> 476 U. S.,
        at 762, there were two purported flaws in the Akron ordinance: the information was designed to dissuade the
        woman from having an abortion and the ordinance imposed \"a rigid requirement that a specific body of
        information be given in all cases, irrespective of the particular needs of the patient . . . .\" <i>Ibid.</i>
    </p>\n<p>To the extent <i>Akron I</i> and <i>Thornburgh</i> find a constitutional violation when the government
        requires, as it does here, the giving of truthful, nonmisleading information about the nature of the procedure,
        the attendant health risks and those of childbirth, and the \"probable gestational age\" of the fetus, those
        cases go too far, are inconsistent with <i>Roe</i> `s acknowledgment of an important interest in potential life,
        and are overruled. This is clear even on the very terms of <i>Akron I</i> and <i>Thornburgh.</i> Those
        decisions, along with <i>Danforth,</i> recognize a substantial government interest justifying a requirement that
        a woman be apprised of the health risks of abortion and childbirth. <i>E. g., </i><i>Danforth, supra,</i> at
        66-67. It cannot be questioned that psychological well-being is a facet of health. Nor can it be doubted that
        most women considering an abortion would deem the impact on the fetus relevant, if not dispositive, to the
        decision. In attempting to ensure that a woman apprehend the full consequences of her decision, the State
        furthers the legitimate purpose of reducing the risk that a woman may elect an abortion, only to discover later,
        with devastating psychological consequences, that her decision was not fully informed. If the information the
        State requires to be made available to the woman is truthful and not misleading, the requirement may be
        permissible.</p>\n<p>We also see no reason why the State may not require doctors to inform a woman seeking an
        abortion of the availability of materials relating to the consequences to the fetus, even when those
        consequences have no direct relation to her health. An example illustrates the point. We would think <span
            class=\"star-pagination\">*883</span> it constitutional for the State to require that in order for there to
        be informed consent to a kidney transplant operation the recipient must be supplied with information about risks
        to the donor as well as risks to himself or herself. A requirement that the physician make available information
        similar to that mandated by the statute here was described in <i>Thornburgh</i> as \"an outright attempt to
        wedge the Commonwealth's message discouraging abortion into the privacy of the informed-consent dialogue between
        the woman and her physician.\" 476 U. S., at 762. We conclude, however, that informed choice need not be defined
        in such narrow terms that all considerations of the effect on the fetus are made irrelevant. As we have made
        clear, we depart from the holdings of <i>Akron I</i> and <i>Thornburgh</i> to the extent that we permit a State
        to further its legitimate goal of protecting the life of the unborn by enacting legislation aimed at ensuring a
        decision that is mature and informed, even when in so doing the State expresses a preference for childbirth over
        abortion. In short, requiring that the woman be informed of the availability of information relating to fetal
        development and the assistance available should she decide to carry the pregnancy to full term is a reasonable
        measure to ensure an informed choice, one which might cause the woman to choose childbirth over abortion. This
        requirement cannot be considered a substantial obstacle to obtaining an abortion, and, it follows, there is no
        undue burden.</p>\n<p>Our prior cases also suggest that the \"straitjacket,\" <i>Thornburgh, supra,</i> at 762
        (quoting <i>Danforth, supra,</i> at 67, n. 8), of particular information which must be given in each case
        interferes with a constitutional right of privacy between a pregnant woman and her physician. As a preliminary
        matter, it is worth noting that the statute now before us does not require a physician to comply with the
        informed consent provisions \"if he or she can demonstrate by a preponderance of the evidence, that he or she
        reasonably believed that furnishing the information would have resulted in a severely <span
            class=\"star-pagination\">*884</span> adverse effect on the physical or mental health of the patient.\" 18
        Pa. Cons. Stat. § 3205 (1990). In this respect, the statute does not prevent the physician from exercising his
        or her medical judgment.</p>\n<p>Whatever constitutional status the doctor-patient relation may have as a
        general matter, in the present context it is derivative of the woman's position. The doctor-patient relation
        does not underlie or override the two more general rights under which the abortion right is justified: the right
        to make family decisions and the right to physical autonomy. On its own, the doctor-patient relation here is
        entitled to the same solicitude it receives in other contexts. Thus, a requirement that a doctor give a woman
        certain information as part of obtaining her consent to an abortion is, for constitutional purposes, no
        different from a requirement that a doctor give certain specific information about any medical procedure.</p>\n
    <p>All that is left of petitioners' argument is an asserted First Amendment right of a physician not to provide
        information about the risks of abortion, and childbirth, in a manner mandated by the State. To be sure, the
        physician's First Amendment rights not to speak are implicated, see <i>Wooley</i> v. <i>Maynard,</i> 430 U. S.
        705 (1977), but only as part of the practice of medicine, subject to reasonable licensing and regulation by the
        State, cf. <i>Whalen</i> v. <i>Roe,</i> 429 U. S. 589, 603 (1977). We see no constitutional infirmity in the
        requirement that the physician provide the information mandated by the State here.</p>\n<p>The Pennsylvania
        statute also requires us to reconsider the holding in <i>Akron I</i> that the State may not require that a
        physician, as opposed to a qualified assistant, provide information relevant to a woman's informed consent. 462
        U. S., at 448. Since there is no evidence on this record that requiring a doctor to give the information as
        provided by the statute would amount in practical terms to a substantial obstacle to a woman seeking an
        abortion, we conclude that it is not <span class=\"star-pagination\">*885</span> an undue burden. Our cases
        reflect the fact that the Constitution gives the States broad latitude to decide that particular functions may
        be performed only by licensed professionals, even if an objective assessment might suggest that those same tasks
        could be performed by others. See <i>Williamson</i> v. <i>Lee Optical of Okla., Inc.,</i> 348 U. S. 483 (1955).
        Thus, we uphold the provision as a reasonable means to ensure that the woman's consent is informed.</p>\n<p>Our
        analysis of Pennsylvania's 24-hour waiting period between the provision of the information deemed necessary to
        informed consent and the performance of an abortion under the undue burden standard requires us to reconsider
        the premise behind the decision in <i>Akron I</i> invalidating a parallel requirement. In <i>Akron I</i> we
        said: \"Nor are we convinced that the State's legitimate concern that the woman's decision be informed is
        reasonably served by requiring a 24-hour delay as a matter of course.\" 462 U. S., at 450. We consider that
        conclusion to be wrong. The idea that important decisions will be more informed and deliberate if they follow
        some period of reflection does not strike us as unreasonable, particularly where the statute directs that
        important information become part of the background of the decision. The statute, as construed by the Court of
        Appeals, permits avoidance of the waiting period in the event of a medical emergency and the record evidence
        shows that in the vast majority of cases, a 24-hour delay does not create any appreciable health risk. In
        theory, at least, the waiting period is a reasonable measure to implement the State's interest in protecting the
        life of the unborn, a measure that does not amount to an undue burden.</p>\n<p>Whether the mandatory 24-hour
        waiting period is nonetheless invalid because in practice it is a substantial obstacle to a woman's choice to
        terminate her pregnancy is a closer question. The findings of fact by the District Court indicate that because
        of the distances many women must travel to reach an abortion provider, the practical effect will often be <span
            class=\"star-pagination\">*886</span> a delay of much more than a day because the waiting period requires
        that a woman seeking an abortion make at least two visits to the doctor. The District Court also found that in
        many instances this will increase the exposure of women seeking abortions to \"the harassment and hostility of
        antiabortion protestors demonstrating outside a clinic.\" 744 F. Supp., at 1351. As a result, the District Court
        found that for those women who have the fewest financial resources, those who must travel long distances, and
        those who have difficulty explaining their whereabouts to husbands, employers, or others, the 24-hour waiting
        period will be \"particularly burdensome.\" <i>Id.,</i> at 1352.</p>\n<p>These findings are troubling in some
        respects, but they do not demonstrate that the waiting period constitutes an undue burden. We do not doubt that,
        as the District Court held, the waiting period has the effect of \"increasing the cost and risk of delay of
        abortions,\" <i>id.,</i> at 1378, but the District Court did not conclude that the increased costs and potential
        delays amount to substantial obstacles. Rather, applying the trimester framework's strict prohibition of all
        regulation designed to promote the State's interest in potential life before viability, see <i>id.,</i> at 1374,
        the District Court concluded that the waiting period does not further the state \"interest in maternal health\"
        and \"infringes the physician's discretion to exercise sound medical judgment,\" <i>id.,</i> at 1378. Yet, as we
        have stated, under the undue burden standard a State is permitted to enact persuasive measures which favor
        childbirth over abortion, even if those measures do not further a health interest. And while the waiting period
        does limit a physician's discretion, that is not, standing alone, a reason to invalidate it. In light of the
        construction given the statute's definition of medical emergency by the Court of Appeals, and the District
        Court's findings, we cannot say that the waiting period imposes a real health risk.</p>\n<p>We also disagree
        with the District Court's conclusion that the \"particularly burdensome\" effects of the waiting period <span
            class=\"star-pagination\">*887</span> on some women require its invalidation. A particular burden is not of
        necessity a substantial obstacle. Whether a burden falls on a particular group is a distinct inquiry from
        whether it is a substantial obstacle even as to the women in that group. And the District Court did not conclude
        that the waiting period is such an obstacle even for the women who are most burdened by it. Hence, on the record
        before us, and in the context of this facial challenge, we are not convinced that the 24-hour waiting period
        constitutes an undue burden.</p>\n<p>We are left with the argument that the various aspects of the informed
        consent requirement are unconstitutional because they place barriers in the way of abortion on demand. Even the
        broadest reading of <i>Roe,</i> however, has not suggested that there is a constitutional right to abortion on
        demand. See, <i>e. g., </i><i>Doe</i> v. <i>Bolton,</i> 410 U. S., at 189. Rather, the right protected by
        <i>Roe</i> is a right to decide to terminate a pregnancy free of undue interference by the State. Because the
        informed consent requirement facilitates the wise exercise of that right, it cannot be classified as an
        interference with the right <i>Roe</i> protects. The informed consent requirement is not an undue burden on that
        right.
    </p>\n<p></p>\n<h2>C</h2>\n<p>Section 3209 of Pennsylvania's abortion law provides, except in cases of
        medical emergency, that no physician shall perform an abortion on a married woman without receiving a signed
        statement from the woman that she has notified her spouse that she is about to undergo an abortion. The woman
        has the option of providing an alternative signed statement certifying that her husband is not the man who
        impregnated her; that her husband could not be located; that the pregnancy is the result of spousal sexual
        assault which she has reported; or that the woman believes that notifying her husband will cause him or someone
        else to inflict bodily injury upon her. A physician who performs an abortion on <span
            class=\"star-pagination\">*888</span> a married woman without receiving the appropriate signed statement
        will have his or her license revoked, and is liable to the husband for damages.</p>\n<p>The District Court heard
        the testimony of numerous expert witnesses, and made detailed findings of fact regarding the effect of this
        statute. These included:</p>\n<blockquote>\"273. The vast majority of women consult their husbands prior to
        deciding to terminate their pregnancy. . . .</blockquote>\n<p>. . . . .</p>\n<blockquote>\"279. The `bodily
        injury' exception could not be invoked by a married woman whose husband, if notified, would, in her reasonable
        belief, threaten to (a) publicize her intent to have an abortion to family, friends or acquaintances; (b)
        retaliate against her in future child custody or divorce proceedings; (c) inflict psychological intimidation or
        emotional harm upon her, her children or other persons; (d) inflict bodily harm on other persons such as
        children, family members or other loved ones; or (e) use his control over finances to deprive of necessary
        monies for herself or her children. . . .</blockquote>\n<p>. . . . .</p>\n<blockquote>\"281. Studies reveal that
        family violence occurs in two million families in the United States. This figure, however, is a conservative one
        that substantially understates (because battering is usually not reported until it reaches life-threatening
        proportions) the actual number of families affected by domestic violence. In fact, researchers estimate that one
        of every two women will be battered at some time in their life. . . .</blockquote>\n<blockquote>\"282. A wife
        may not elect to notify her husband of her intention to have an abortion for a variety of reasons, including the
        husband's illness, concern about her own health, the imminent failure of the marriage, or the husband's absolute
        opposition to the abortion. . . .</blockquote>\n<blockquote>\"283. The required filing of the spousal consent
        form would require plaintiff-clinics to change their counseling <span class=\"star-pagination\">*889</span>
        procedures and force women to reveal their most intimate decision-making on pain of criminal sanctions. The
        confidentiality of these revelations could not be guaranteed, since the woman's records are not immune from
        subpoena. . . .</blockquote>\n<blockquote>\"284. Women of all class levels, educational backgrounds, and racial,
        ethnic and religious groups are battered. . . .</blockquote>\n<blockquote>\"285. Wife-battering or abuse can
        take on many physical and psychological forms. The nature and scope of the battering can cover a broad range of
        actions and be gruesome and torturous. . . .</blockquote>\n<blockquote>\"286. Married women, victims of
        battering, have been killed in Pennsylvania and throughout the United States. . . .</blockquote>\n<blockquote>
        \"287. Battering can often involve a substantial amount of sexual abuse, including marital rape and sexual
        mutilation. . . .</blockquote>\n<blockquote>\"288. In a domestic abuse situation, it is common for the battering
        husband to also abuse the children in an attempt to coerce the wife. . . .</blockquote>\n<blockquote>\"289. Mere
        notification of pregnancy is frequently a flashpoint for battering and violence within the family. The number of
        battering incidents is high during the pregnancy and often the worst abuse can be associated with pregnancy. . .
        . The battering husband may deny parentage and use the pregnancy as an excuse for abuse. . . .</blockquote>\n
    <blockquote>\"290. Secrecy typically shrouds abusive families. Family members are instructed not to tell anyone,
        especially police or doctors, about the abuse and violence. Battering husbands often threaten their wives or her
        children with further abuse if she tells an outsider of the violence and tells her that nobody will believe her.
        A battered woman, therefore, is highly unlikely to disclose <span class=\"star-pagination\">*890</span> the
        violence against her for fear of retaliation by the abuser. . . .</blockquote>\n<blockquote>\"291. Even when
        confronted directly by medical personnel or other helping professionals, battered women often will not admit to
        the battering because they have not admitted to themselves that they are battered. . . .</blockquote>\n<p>. . .
        . .</p>\n<blockquote>\"294. A woman in a shelter or a safe house unknown to her husband is not `reasonably
        likely' to have bodily harm inflicted upon her by her batterer, however her attempt to notify her husband
        pursuant to section 3209 could accidentally disclose her whereabouts to her husband. Her fear of future
        ramifications would be realistic under the circumstances.</blockquote>\n<blockquote>\"295. Marital rape is
        rarely discussed with others or reported to law enforcement authorities, and of those reported only few are
        prosecuted. . . .</blockquote>\n<blockquote>\"296. It is common for battered women to have sexual intercourse
        with their husbands to avoid being battered. While this type of coercive sexual activity would be spousal sexual
        assault as defined by the Act, many women may not consider it to be so and others would fear disbelief. . . .
    </blockquote>\n<blockquote>\"297. The marital rape exception to section 3209 cannot be claimed by women who are
        victims of coercive sexual behavior other than penetration. The 90-day reporting requirement of the spousal
        sexual assault statute, 18 Pa. Con. Stat. Ann. § 3218(c), further narrows the class of sexually abused wives who
        can claim the exception, since many of these women may be psychologically unable to discuss or report the rape
        for several years after the incident. . . .</blockquote>\n<blockquote>\"298. Because of the nature of the
        battering relationship, battered women are unlikely to avail themselves of the exceptions to section 3209 of the
        Act, regardless of <span class=\"star-pagination\">*891</span> whether the section applies to them.\" 744 F.
        Supp., at 1360-1362 (footnote omitted).</blockquote>\n<p>These findings are supported by studies of domestic
        violence. The American Medical Association (AMA) has published a summary of the recent research in this field,
        which indicates that in an average 12-month period in this country, approximately two million women are the
        victims of severe assaults by their male partners. In a 1985 survey, women reported that nearly one of every
        eight husbands had assaulted their wives during the past year. The AMA views these figures as \"marked
        underestimates,\" because the nature of these incidents discourages women from reporting them, and because
        surveys typically exclude the very poor, those who do not speak English well, and women who are homeless or in
        institutions or hospitals when the survey is conducted. According to the AMA, \"[r]esearchers on family violence
        agree that the true incidence of partner violence is probably <i>double</i> the above estimates; or four million
        severely assaulted women per year. Studies on prevalence suggest that from one-fifth to one-third of all women
        will be physically assaulted by a partner or ex-partner during their lifetime.\" AMA Council on Scientific
        Affairs, Violence Against Women 7 (1991) (emphasis in original). Thus on an average day in the United States,
        nearly 11,000 women are severely assaulted by their male partners. Many of these incidents involve sexual
        assault. <i>Id.,</i> at 3-4; Shields &amp; Hanneke,</p>\n<p>Battered Wives' Reactions to Marital Rape, in The
        Dark Side of Families: Current Family Violence Research 131, 144 (D. Finkelhor, R. Gelles, G. Hataling, &amp; M.
        Straus eds. 1983). In families where wifebeating takes place, moreover, child abuse is often present as well.
        Violence Against Women, <i>supra,</i> at 12.</p>\n<p>Other studies fill in the rest of this troubling picture.
        Physical violence is only the most visible form of abuse. Psychological abuse, particularly forced social and
        economic isolation of women, is also common. L. Walker, The Battered <span class=\"star-pagination\">*892</span>
        Woman Syndrome 27-28 (1984). Many victims of domestic violence remain with their abusers, perhaps because they
        perceive no superior alternative. Herbert, Silver, &amp; Ellard, Coping with an Abusive Relationship: I. How and
        Why do Women Stay?, 53 J. Marriage &amp; the Family 311 (1991). Many abused women who find temporary refuge in
        shelters return to their husbands, in large part because they have no other source of income. Aguirre, Why Do
        They Return? Abused Wives in Shelters, 30 J. Nat. Assn. of Social Workers 350, 352 (1985). Returning to one's
        abuser can be dangerous. Recent Federal Bureau of Investigation statistics disclose that 8.8 percent of all
        homicide victims in the United States are killed by their spouses. Mercy &amp; Saltzman, Fatal Violence Among
        Spouses in the United States, 1976-85, 79 Am. J. Public Health 595 (1989). Thirty percent of female homicide
        victims are killed by their male partners. Domestic Violence: Terrorism in the Home, Hearing before the
        Subcommittee on Children, Family, Drugs and Alcoholism of the Senate Committee on Labor and Human Resources,
        101st Cong., 2d Sess., 3 (1990).</p>\n<p>The limited research that has been conducted with respect to notifying
        one's husband about an abortion, although involving samples too small to be representative, also supports the
        District Court's findings of fact. The vast majority of women notify their male partners of their decision to
        obtain an abortion. In many cases in which married women do not notify their husbands, the pregnancy is the
        result of an extramarital affair. Where the husband is the father, the primary reason women do not notify their
        husbands is that the husband and wife are experiencing marital difficulties, often accompanied by incidents of
        violence. Ryan &amp; Plutzer, When Married Women Have Abortions: Spousal Notification and Marital Interaction,
        51 J. Marriage &amp; the Family 41, 44 (1989).</p>\n<p>This information and the District Court's findings
        reinforce what common sense would suggest. In wellfunctioning <span class=\"star-pagination\">*893</span>
        marriages, spouses discuss important intimate decisions such as whether to bear a child. But there are millions
        of women in this country who are the victims of regular physical and psychological abuse at the hands of their
        husbands. Should these women become pregnant, they may have very good reasons for not wishing to inform their
        husbands of their decision to obtain an abortion. Many may have justifiable fears of physical abuse, but may be
        no less fearful of the consequences of reporting prior abuse to the Commonwealth of Pennsylvania. Many may have
        a reasonable fear that notifying their husbands will provoke further instances of child abuse; these women are
        not exempt from § 3209's notification requirement. Many may fear devastating forms of psychological abuse from
        their husbands, including verbal harassment, threats of future violence, the destruction of possessions,
        physical confinement to the home, the withdrawal of financial support, or the disclosure of the abortion to
        family and friends. These methods of psychological abuse may act as even more of a deterrent to notification
        than the possibility of physical violence, but women who are the victims of the abuse are not exempt from §
        3209's notification requirement. And many women who are pregnant as a result of sexual assaults by their
        husbands will be unable to avail themselves of the exception for spousal sexual assault, § 3209(b)(3), because
        the exception requires that the woman have notified law enforcement authorities within 90 days of the assault,
        and her husband will be notified of her report once an investigation begins, § 3128(c). If anything in this
        field is certain, it is that victims of spousal sexual assault are extremely reluctant to report the abuse to
        the government; hence, a great many spousal rape victims will not be exempt from the notification requirement
        imposed by § 3209.</p>\n<p>The spousal notification requirement is thus likely to prevent a significant number
        of women from obtaining an abortion. It does not merely make abortions a little more difficult or expensive to
        obtain; for many women, it will impose <span class=\"star-pagination\">*894</span> a substantial obstacle. We
        must not blind ourselves to the fact that the significant number of women who fear for their safety and the
        safety of their children are likely to be deterred from procuring an abortion as surely as if the Commonwealth
        had outlawed abortion in all cases.</p>\n<p>Respondents attempt to avoid the conclusion that § 3209 is invalid
        by pointing out that it imposes almost no burden at all for the vast majority of women seeking abortions. They
        begin by noting that only about 20 percent of the women who obtain abortions are married. They then note that of
        these women about 95 percent notify their husbands of their own volition. Thus, respondents argue, the effects
        of § 3209 are felt by only one percent of the women who obtain abortions. Respondents argue that since some of
        these women will be able to notify their husbands without adverse consequences or will qualify for one of the
        exceptions, the statute affects fewer than one percent of women seeking abortions. For this reason, it is
        asserted, the statute cannot be invalid on its face. See Brief for Respondents 83-86. We disagree with
        respondents' basic method of analysis.</p>\n<p>The analysis does not end with the one percent of women upon whom
        the statute operates; it begins there. Legislation is measured for consistency with the Constitution by its
        impact on those whose conduct it affects. For example, we would not say that a law which requires a newspaper to
        print a candidate's reply to an unfavorable editorial is valid on its face because most newspapers would adopt
        the policy even absent the law. See <i>Miami Herald Publishing Co.</i> v. <i>Tornillo,</i> 418 U. S. 241 (1974).
        The proper focus of constitutional inquiry is the group for whom the law is a restriction, not the group for
        whom the law is irrelevant.</p>\n<p>Respondents' argument itself gives implicit recognition to this principle,
        at one of its critical points. Respondents speak of the one percent of women seeking abortions who are married
        and would choose not to notify their husbands of their plans. By selecting as the controlling class women <span
            class=\"star-pagination\">*895</span> who wish to obtain abortions, rather than all women or all pregnant
        women, respondents in effect concede that § 3209 must be judged by reference to those for whom it is an actual
        rather than an irrelevant restriction. Of course, as we have said, § 3209's real target is narrower even than
        the class of women seeking abortions identified by the State: it is married women seeking abortions who do not
        wish to notify their husbands of their intentions and who do not qualify for one of the statutory exceptions to
        the notice requirement. The unfortunate yet persisting conditions we document above will mean that in a large
        fraction of the cases in which § 3209 is relevant, it will operate as a substantial obstacle to a woman's choice
        to undergo an abortion. It is an undue burden, and therefore invalid.</p>\n<p>This conclusion is in no way
        inconsistent with our decisions upholding parental notification or consent requirements. See, <i>e. g.,
        </i><i>Akron II,</i> 497 U. S., at 510-519; <i>Bellotti</i> v. <i>Baird,</i> 443 U. S. 622 (1979) <i>(Bellotti
            II)</i><i>; </i><i>Planned Parenthood of Central Mo.</i> v. <i>Danforth,</i> 428 U. S., at 74. Those
        enactments, and our judgment that they are constitutional, are based on the quite reasonable assumption that
        minors will benefit from consultation with their parents and that children will often not realize that their
        parents have their best interests at heart. We cannot adopt a parallel assumption about adult women.</p>\n<p>We
        recognize that a husband has a \"deep and proper concern and interest . . . in his wife's pregnancy and in the
        growth and development of the fetus she is carrying.\" <i>Danforth, supra,</i> at 69. With regard to the
        children he has fathered and raised, the Court has recognized his \"cognizable and substantial\" interest in
        their custody. <i>Stanley</i> v. <i>Illinois,</i> 405 U. S. 645, 651-652 (1972); see also <i>Quilloin</i> v.
        <i>Walcott,</i> 434 U. S. 246 (1978); <i>Caban</i> v. <i>Mohammed,</i> 441 U. S. 380 (1979); <i>Lehr</i> v.
        <i>Robertson,</i> 463 U. S. 248 (1983). If these cases concerned a State's ability to require the mother to
        notify the father before taking some action with respect to a living <span class=\"star-pagination\">*896</span>
        child raised by both, therefore, it would be reasonable to conclude as a general matter that the father's
        interest in the welfare of the child and the mother's interest are equal.
    </p>\n<p>Before birth, however, the
        issue takes on a very different cast. It is an inescapable biological fact that state regulation with respect to
        the child a woman is carrying will have a far greater impact on the mother's liberty than on the father's. The
        effect of state regulation on a woman's protected liberty is doubly deserving of scrutiny in such a case, as the
        State has touched not only upon the private sphere of the family but upon the very bodily integrity of the
        pregnant woman. Cf. <i>Cruzan</i> v. <i>Director, Mo. Dept. of Health,</i> 497 U. S., at 281. The Court has held
        that \"when the wife and the husband disagree on this decision, the view of only one of the two marriage
        partners can prevail. Inasmuch as it is the woman who physically bears the child and who is the more directly
        and immediately affected by the pregnancy, as between the two, the balance weighs in her favor.\" <i>Danforth,
            supra,</i> at 71. This conclusion rests upon the basic nature of marriage and the nature of our
        Constitution: \"[T]he marital couple is not an independent entity with a mind and heart of its own, but an
        association of two individuals each with a separate intellectual and emotional makeup. If the right of privacy
        means anything, it is the right of the <i>individual,</i> married or single, to be free from unwarranted
        governmental intrusion into matters so fundamentally affecting a person as the decision whether to bear or beget
        a child.\" <i>Eisenstadt</i> v. <i>Baird,</i> 405 U. S., at 453 (emphasis in original). The Constitution
        protects individuals, men and women alike, from unjustified state interference, even when that interference is
        enacted into law for the benefit of their spouses.</p>\n<p>There was a time, not so long ago, when a different
        understanding of the family and of the Constitution prevailed. In <i>Bradwell</i> v. <i>State,</i> 16 Wall. 130
        (1873), three Members of this <span class=\"star-pagination\">*897</span> Court reaffirmed the common-law
        principle that \"a woman had no legal existence separate from her husband, who was regarded as her head and
        representative in the social state; and, notwithstanding some recent modifications of this civil status, many of
        the special rules of law flowing from and dependent upon this cardinal principle still exist in full force in
        most States.\" <i>Id.,</i> at 141 (Bradley, J., joined by Swayne and Field, JJ., concurring in judgment). Only
        one generation has passed since this Court observed that \"woman is still regarded as the center of home and
        family life,\" with attendant \"special responsibilities\" that precluded full and independent legal status
        under the Constitution. <i>Hoyt</i> v. <i>Florida,</i> 368 U. S. 57, 62 (1961). These views, of course, are no
        longer consistent with our understanding of the family, the individual, or the Constitution.</p>\n<p>In keeping
        with our rejection of the common-law understanding of a woman's role within the family, the Court held in
        <i>Danforth</i> that the Constitution does not permit a State to require a married woman to obtain her husband's
        consent before undergoing an abortion. 428 U. S., at 69. The principles that guided the Court in <i>Danforth</i>
        should be our guides today. For the great many women who are victims of abuse inflicted by their husbands, or
        whose children are the victims of such abuse, a spousal notice requirement enables the husband to wield an
        effective veto over his wife's decision. Whether the prospect of notification itself deters such women from
        seeking abortions, or whether the husband, through physical force or psychological pressure or economic
        coercion, prevents his wife from obtaining an abortion until it is too late, the notice requirement will often
        be tantamount to the veto found unconstitutional in <i>Danforth.</i> The women most affected by this lawthose
        who most reasonably fear the consequences of notifying their husbands that they are pregnantare in the gravest
        danger.
    </p>\n<p><span class=\"star-pagination\">*898</span> The husband's interest in the life of the child his
        wife is carrying does not permit the State to empower him with this troubling degree of authority over his wife.
        The contrary view leads to consequences reminiscent of the common law. A husband has no enforceable right to
        require a wife to advise him before she exercises her personal choices. If a husband's interest in the potential
        life of the child outweighs a wife's liberty, the State could require a married woman to notify her husband
        before she uses a postfertilization contraceptive. Perhaps next in line would be a statute requiring pregnant
        married women to notify their husbands before engaging in conduct causing risks to the fetus. After all,if the
        husband's interest in the fetus' safety is a sufficient predicate for state regulation, the State could
        reasonably conclude that pregnant wives should notify their husbands before drinking alcohol or smoking. Perhaps
        married women should notify their husbands before using contraceptives or before undergoing any type of surgery
        that may have complications affecting the husband's interest in his wife's reproductive organs. And if a
        husband's interest justifies notice in any of these cases, one might reasonably argue that it justifies exactly
        what the <i>Danforth</i> Court held it did not justifya requirement of the husband's consent as well. A State
        may not give to a man the kind of dominion over his wife that parents exercise over their children.</p>\n<p>
        Section 3209 embodies a view of marriage consonant with the common-law status of married women but repugnant to
        our present understanding of marriage and of the nature of the rights secured by the Constitution. Women do not
        lose their constitutionally protected liberty when they marry. The Constitution protects all individuals, male
        or female, married or unmarried, from the abuse of governmental power, even where that power is employed for the
        supposed benefit of a member of the individual's family. These considerations confirm our conclusion that § 3209
        is invalid.</p>\n<p></p>\n<h2>\n<span class=\"star-pagination\">*899</span> D</h2>\n<p>We next consider the
        parental consent provision. Except in a medical emergency, an unemancipated young woman under 18 may not obtain
        an abortion unless she and one of her parents (or guardian) provides informed consent as defined above. If
        neither a parent nor a guardian provides consent, a court may authorize the performance of an abortion upon a
        determination that the young woman is mature and capable of giving informed consent and has in fact given her
        informed consent, or that an abortion would be in her best interests.</p>\n<p>We have been over most of this
        ground before. Our cases establish, and we reaffirm today, that a State may require a minor seeking an abortion
        to obtain the consent of a parent or guardian, provided that there is an adequate judicial bypass procedure.
        See, <i>e. g., </i><i>Akron II,</i> 497 U. S., at 510-519; <i>Hodgson,</i> 497 U. S., at 461 (O'Connor, J.,
        concurring in part and concurring in judgment in part); <i>id.,</i> at 497-501 (Kennedy, J., concurring in
        judgment in part and dissenting in part); <i>Akron I,</i> 462 U. S., at 440; <i>Bellotti II,</i> 443 U. S., at
        643-644 (plurality opinion). Under these precedents, in our view, the one-parent consent requirement and
        judicial bypass procedure are constitutional.</p>\n<p>The only argument made by petitioners respecting this
        provision and to which our prior decisions do not speak is the contention that the parental consent requirement
        is invalid because it requires informed parental consent. For the most part, petitioners' argument is a reprise
        of their argument with respect to the informed consent requirement in general, and we reject it for the reasons
        given above. Indeed, some of the provisions regarding informed consent have particular force with respect to
        minors: the waiting period, for example, may provide the parent or parents of a pregnant young woman the
        opportunity to consult with her in private, and to discuss the consequences of her decision in <span
            class=\"star-pagination\">*900</span> the context of the values and moral or religious principles of their
        family. See <i>Hodgson, supra,</i> at 448-449 (opinion of Stevens, J.).</p>\n<p></p>\n<h2>E</h2>\n<p>Under the
        recordkeeping and reporting requirements of the statute, every facility which performs abortions is required to
        file a report stating its name and address as well as the name and address of any related entity, such as a
        controlling or subsidiary organization. In the case of statefunded institutions, the information becomes public.
    </p>\n<p>For each abortion performed, a report must be filed identifying: the physician (and the second physician
        where required); the facility; the referring physician or agency; the woman's age; the number of prior
        pregnancies and prior abortions she has had; gestational age; the type of abortion procedure; the date of the
        abortion; whether there were any pre-existing medical conditions which would complicate pregnancy; medical
        complications with the abortion; where applicable, the basis for the determination that the abortion was
        medically necessary; the weight of the aborted fetus; and whether the woman was married, and if so, whether
        notice was provided or the basis for the failure to give notice. Every abortion facility must also file
        quarterly reports showing the number of abortions performed broken down by trimester. See 18 Pa. Cons. Stat. §§
        3207, 3214 (1990). In all events, the identity of each woman who has had an abortion remains confidential.</p>\n
    <p>In <i>Danforth,</i> 428 U. S., at 80, we held that recordkeeping and reporting provisions \"that are reasonably
        directed to the preservation of maternal health and that properly respect a patient's confidentiality and
        privacy are permissible.\" We think that under this standard, all the provisions at issue here, except that
        relating to spousal notice, are constitutional. Although they do not relate to the State's interest in informing
        the woman's choice, they do relate to health. The collection of information with respect to actual patients
        <span class=\"star-pagination\">*901</span> is a vital element of medical research, and so it cannot be said
        that the requirements serve no purpose other than to make abortions more difficult. Nor do we find that the
        requirements impose a substantial obstacle to a woman's choice. At most they might increase the cost of some
        abortions by a slight amount. While at some point increased cost could become a substantial obstacle, there is
        no such showing on the record before us.
    </p>\n<p>Subsection (12) of the reporting provision requires the
        reporting of, among other things, a married woman's \"reason for failure to provide notice\" to her husband. §
        3214(a)(12). This provision in effect requires women, as a condition of obtaining an abortion, to provide the
        Commonwealth with the precise information we have already recognized that many women have pressing reasons not
        to reveal. Like the spousal notice requirement itself, this provision places an undue burden on a woman's
        choice, and must be invalidated for that reason.</p>\n<p></p>\n<h2>VI</h2>\n<p>Our Constitution is a covenant
        running from the first generation of Americans to us and then to future generations. It is a coherent
        succession. Each generation must learn anew that the Constitution's written terms embody ideas and aspirations
        that must survive more ages than one. We accept our responsibility not to retreat from interpreting the full
        meaning of the covenant in light of all of our precedents. We invoke it once again to define the freedom
        guaranteed by the Constitution's own promise, the promise of liberty.</p>\n<p></p>\n<h2>* * *</h2>\n<p>The
        judgment in No. 91-902 is affirmed. The judgment in No. 91-744 is affirmed in part and reversed in part, and the
        case is remanded for proceedings consistent with this opinion, including consideration of the question of
        severability.</p>\n<p><i>It is so ordered.</i> </p>\n<p><span class=\"star-pagination\">*902</span> APPENDIX TO
        OPINION OF O'CONNOR, KENNEDY, AND SOUTER, JJ.</p>\n<p>Selected Provisions of the 1988 and 1989 Amendments to the
    </p>\n<blockquote>Pennsylvania Abortion Control Act of 1982 18 PA. CONS. STAT. (1990).</blockquote>\n<p>\"§ 3203.
        Definitions.</p>\n<p>. . . . .</p>\n<p>\"`Medical emergency.' That condition which, on the basis of the
        physician's good faith clinical judgment, so complicates the medical condition of a pregnant woman as to
        necessitate the immediate abortion of her pregnancy to avert her death or for which a delay will create serious
        risk of substantial and irreversible impairment of major bodily function.\"</p>\n<p>\"§ 3205. Informed consent.
    </p>\n<p>\"(a) General rule.No abortion shall be performed or induced except with the voluntary and informed
        consent of the woman upon whom the abortion is to be performed or induced. Except in the case of a medical
        emergency, consent to an abortion is voluntary and informed if and only if:</p>\n<blockquote>\"(1) At least 24
        hours prior to the abortion, the physician who is to perform the abortion or the referring physician has orally
        informed the woman of:</blockquote>\n<blockquote>\"(i) The nature of the proposed procedure or treatment and of
        those risks and alternatives to the procedure or treatment that a reasonable patient would consider material to
        the decision of whether or not to undergo the abortion.</blockquote>\n<blockquote>\"(ii) The probable
        gestational age of the unborn child at the time the abortion is to be performed.</blockquote>\n<blockquote>
        \"(iii) The medical risks associated with carrying her child to term.</blockquote>\n<blockquote>\"(2) At least
        24 hours prior to the abortion, the physician who is to perform the abortion or the referring physician, or a
        qualified physician assistant, health care practitioner, technician or social worker to whom the responsibility
        <span class=\"star-pagination\">*903</span> has been delegated by either physician, has informed the pregnant
        woman that:
    </blockquote>\n<blockquote>\"(i) The department publishes printed materials which describe the unborn
        child and list agencies which offer alternatives to abortion and that she has a right to review the printed
        materials and that a copy will be provided to her free of charge if she chooses to review it.</blockquote>\n
    <blockquote>\"(ii) Medical assistance benefits may be available for prenatal care, childbirth and neonatal care, and
        that more detailed information on the availability of such assistance is contained in the printed materials
        published by the department.</blockquote>\n<blockquote>\"(iii) The father of the unborn child is liable to
        assist in the support of her child, even in instances where he has offered to pay for the abortion. In the case
        of rape, this information may be omitted.</blockquote>\n<blockquote>\"(3) A copy of the printed materials has
        been provided to the woman if she chooses to view these materials.</blockquote>\n<blockquote>\"(4) The pregnant
        woman certifies in writing, prior to the abortion, that the information required to be provided under paragraphs
        (1), (2) and (3) has been provided.</blockquote>\n<p>\"(b) Emergency.Where a medical emergency compels the
        performance of an abortion, the physician shall inform the woman, prior to the abortion if possible, of the
        medical indications supporting his judgment that an abortion is necessary to avert her death or to avert
        substantial and irreversible impairment of major bodily function.</p>\n<p>\"(c) Penalty.Any physician who
        violates the provisions of this section is guilty of `unprofessional conduct' and his license for the practice
        of medicine and surgery shall be subject to suspension or revocation in accordance with procedures provided
        under the act of October 5, 1978 (P. L. 1109, No. 261), known as the Osteopathic Medical Practice Act, the <span
            class=\"star-pagination\">*904</span> act of December 20, 1985 (P. L. 457, No. 112), known as the Medical
        Practice Act of 1985, or their successor acts. Any physician who performs or induces an abortion without first
        obtaining the certification required by subsection (a)(4) or with knowledge or reason to know that the informed
        consent of the woman has not been obtained shall for the first offense be guilty of a summary offense and for
        each subsequent offense be guilty of a misdemeanor of the third degree. No physician shall be guilty of
        violating this section for failure to furnish the information required by subsection (a) if he or she can
        demonstrate, by a preponderance of the evidence, that he or she reasonably believed that furnishing the
        information would have resulted in a severely adverse effect on the physical or mental health of the patient.
    </p>\n<p>\"(d) Limitation on civil liability.Any physician who complies with the provisions of this section may not
        be held civilly liable to his patient for failure to obtain informed consent to the abortion within the meaning
        of that term as defined by the act of October 15, 1975 (P. L. 390, No. 111), known as the Health Care Services
        Malpractice Act.\"</p>\n<p>\"§ 3206. Parental consent.</p>\n<p>\"(a) General rule.Except in the case of a
        medical emergency or except as provided in this section, if a pregnant woman is less than 18 years of age and
        not emancipated, or if she has been adjudged an incompetent under 20 Pa. C. S. § 5511 (relating to petition and
        hearing; examination by court-appointed physician), a physician shall not perform an abortion upon her unless,
        in the case of a woman who is less than 18 years of age, he first obtains the informed consent both of the
        pregnant woman and of one of her parents; or, in the case of a woman who is incompetent, he first obtains the
        informed consent of her guardian. In deciding whether to grant such consent, a pregnant woman's parent or
        guardian shall consider only their child's or ward's best interests. In the case of a pregnancy that is the
        result of incest, where <span class=\"star-pagination\">*905</span> the father is a party to the incestuous act,
        the pregnant woman need only obtain the consent of her mother.</p>\n<p>\"(b) Unavailability of parent or
        guardian.If both parents have died or are otherwise unavailable to the physician within a reasonable time and
        in a reasonable manner, consent of the pregnant woman's guardian or guardians shall be sufficient. If the
        pregnant woman's parents are divorced, consent of the parent having custody shall be sufficient. If neither any
        parent nor a legal guardian is available to the physician within a reasonable time and in a reasonable manner,
        consent of any adult person standing in loco parentis shall be sufficient.</p>\n<p>\"(c) Petition to the court
        for consent.If both of the parents or guardians of the pregnant woman refuse to consent to the performance of
        an abortion or if she elects not to seek the consent of either of her parents or of her guardian, the court of
        common pleas of the judicial district in which the applicant resides or in which the abortion is sought shall,
        upon petition or motion, after an appropriate hearing, authorize a physician to perform the abortion if the
        court determines that the pregnant woman is mature and capable of giving informed consent to the proposed
        abortion, and has, in fact, given such consent.</p>\n<p>\"(d) Court order.If the court determines that the
        pregnant woman is not mature and capable of giving informed consent or if the pregnant woman does not claim to
        be mature and capable of giving informed consent, the court shall determine whether the performance of an
        abortion upon her would be in her best interests. If the court determines that the performance of an abortion
        would be in the best interests of the woman, it shall authorize a physician to perform the abortion.</p>\n<p>
        \"(e) Representation in proceedings.The pregnant woman may participate in proceedings in the court on her own
        behalf and the court may appoint a guardian ad litem to assist her. The court shall, however, advise her that
        she has <span class=\"star-pagination\">*906</span> a right to court appointed counsel, and shall provide her
        with such counsel unless she wishes to appear with private counsel or has knowingly and intelligently waived
        representation by counsel.\"</p>\n<p>\"§ 3207. Abortion facilities.</p>\n<p>. . . . .</p>\n<p>\"(b)
        Reports.Within 30 days after the effective date of this chapter, every facility at which abortions are
        performed shall file, and update immediately upon any change, a report with the department, containing the
        following information:</p>\n<p>\"(1) Name and address of the facility.</p>\n<blockquote>\"(2) Name and address
        of any parent, subsidiary or affiliated organizations, corporations or associations.</blockquote>\n<blockquote>
        \"(3) Name and address of any parent, subsidiary or affiliated organizations, corporations or associations
        having contemporaneous commonality of ownership, beneficial interest, directorship or officership with any other
        facility.</blockquote>\n<p>The information contained in those reports which are filed pursuant to this
        subsection by facilities which receive Stateappropriated funds during the 12-calendar-month period immediately
        preceding a request to inspect or copy such reports shall be deemed public information. Reports filed by
        facilities which do not receive State-appropriated funds shall only be available to law enforcement officials,
        the State Board of Medicine and the State Board of Osteopathic Medicine for use in the performance of their
        official duties. Any facility failing to comply with the provisions of this subsection shall be assessed by the
        department a fine of $500 for each day it is in violation hereof.\"</p>\n<p>\"§ 3208. Printed information.</p>\n
    <p>\"(a) General rule.The department shall cause to be published in English, Spanish and Vietnamese, within 60 days
        after this chapter becomes law, and shall update on an annual basis, the following easily comprehensible printed
        materials:</p>\n<blockquote>\n<span class=\"star-pagination\">*907</span> \"(1) Geographically indexed materials
        designed to inform the woman of public and private agencies and services available to assist a woman through
        pregnancy, upon childbirth and while the child is dependent, including adoption agencies, which shall include a
        comprehensive list of the agencies available, a description of the services they offer and a description of the
        manner, including telephone numbers, in which they might be contacted, or, at the option of the department,
        printed materials including a toll-free 24-hour a day telephone number which may be called to obtain, orally,
        such a list and description of agencies in the locality of the caller and of the services they offer. The
        materials shall provide information on the availability of medical assistance benefits for prenatal care,
        childbirth and neonatal care, and state that it is unlawful for any individual to coerce a woman to undergo
        abortion, that any physician who performs an abortion upon a woman without obtaining her informed consent or
        without according her a private medical consultation may be liable to her for damages in a civil action at law,
        that the father of a child is liable to assist in the support of that child, even in instances where the father
        has offered to pay for an abortion and that the law permits adoptive parents to pay costs of prenatal care,
        childbirth and neonatal care.</blockquote>\n<blockquote>\"(2) Materials designed to inform the woman of the
        probable anatomical and physiological characteristics of the unborn child at two-week gestational increments
        from fertilization to full term, including pictures representing the development of unborn children at two-week
        gestational increments, and any relevant information on the possibility of the unborn child's survival; provided
        that any such pictures or drawings must contain the dimensions of the fetus and must be realistic and
        appropriate for the woman's stage of pregnancy. The materials shall be objective, non-judgmental and designed
        <span class=\"star-pagination\">*908</span> to convey only accurate scientific information about the unborn
        child at the various gestational ages. The material shall also contain objective information describing the
        methods of abortion procedures commonly employed, the medical risks commonly associated with each such
        procedure, the possible detrimental psychological effects of abortion and the medical risks commonly associated
        with each such procedure and the medical risks commonly associated with carrying a child to term.
    </blockquote>\n
    <p>\"(b) Format.The materials shall be printed in a typeface large enough to be clearly legible.</p>\n<p>\"(c) Free
        distribution.The materials required under this section shall be available at no cost from the department upon
        request and in appropriate number to any person, facility or hospital.\"</p>\n<p>\"§ 3209. Spousal notice.</p>\n
    <p>\"(a) Spousal notice required.In order to further the Commonwealth's interest in promoting the integrity of the
        marital relationship and to protect a spouse's interests in having children within marriage and in protecting
        the prenatal life of that spouse's child, no physician shall perform an abortion on a married woman, except as
        provided in subsections (b) and (c), unless he or she has received a signed statement, which need not be
        notarized, from the woman upon whom the abortion is to be performed, that she has notified her spouse that she
        is about to undergo an abortion. The statement shall bear a notice that any false statement made therein is
        punishable by law.</p>\n<p>\"(b) Exceptions.The statement certifying that the notice required by subsection (a)
        has been given need not be furnished where the woman provides the physician a signed statement certifying at
        least one of the following:</p>\n<p>\"(1) Her spouse is not the father of the child.</p>\n<blockquote>\"(2) Her
        spouse, after diligent effort, could not be located.</blockquote>\n<blockquote>\n<span
            class=\"star-pagination\">*909</span> \"(3) The pregnancy is a result of spousal sexual assault as described
        in section 3128 (relating to spousal sexual assault), which has been reported to a law enforcement agency having
        the requisite jurisdiction.</blockquote>\n<blockquote>\"(4) The woman has reason to believe that the furnishing
        of notice to her spouse is likely to result in the infliction of bodily injury upon her by her spouse or by
        another individual.</blockquote>\n<p>Such statement need not be notarized, but shall bear a notice that any
        false statements made therein are punishable by law.</p>\n<p>\"(c) Medical emergency.The requirements of
        subsection (a) shall not apply in case of a medical emergency.</p>\n<p>\"(d) Forms.The department shall cause
        to be published, forms which may be utilized for purposes of providing the signed statements required by
        subsections (a) and (b). The department shall distribute an adequate supply of such forms to all abortion
        facilities in this Commonwealth.</p>\n<p>\"(e) Penalty; civil action.Any physician who violates the provisions
        of this section is guilty of `unprofessional conduct,' and his or her license for the practice of medicine and
        surgery shall be subject to suspension or revocation in accordance with procedures provided under the act of
        October 5, 1978 (P. L. 1109, No. 261), known as the Osteopathic Medical Practice Act, the act of December 20,
        1985 (P. L. 457, No. 112), known as the Medical Practice Act of 1985, or their successor acts. In addition, any
        physician who knowingly violates the provisions of this section shall be civilly liable to the spouse who is the
        father of the aborted child for any damages caused thereby and for punitive damages in the amount of $5,000, and
        the court shall award a prevailing plaintiff a reasonable attorney fee as part of costs.\"</p>\n<p>\"§ 3214.
        Reporting.</p>\n<p>\"(a) General rule.For the purpose of promotion of maternal health and life by adding to the
        sum of medical and <span class=\"star-pagination\">*910</span> public health knowledge through the compilation
        of relevant data, and to promote the Commonwealth's interest in protection of the unborn child, a report of each
        abortion performed shall be made to the department on forms prescribed by it. The report forms shall not
        identify the individual patient by name and shall include the following information:</p>\n<blockquote>\"(1)
        Identification of the physician who performed the abortion, the concurring physician as required by section
        3211(c)(2) (relating to abortion on unborn child of 24 or more weeks gestational age), the second physician as
        required by section 3211(c)(5) and the facility where the abortion was performed and of the referring physician,
        agency or service, if any.</blockquote>\n<p>\"(2) The county and state in which the woman resides.</p>\n<p>\"(3)
        The woman's age.</p>\n<blockquote>\"(4) The number of prior pregnancies and prior abortions of the woman.
    </blockquote>\n<blockquote>\"(5) The gestational age of the unborn child at the time of the abortion.</blockquote>\n
    <blockquote>\"(6) The type of procedure performed or prescribed and the date of the abortion.</blockquote>\n
    <blockquote>\"(7) Pre-existing medical conditions of the woman which would complicate pregnancy, if any, and if
        known, any medical complication which resulted from the abortion itself.</blockquote>\n<blockquote>\"(8) The
        basis for the medical judgment of the physician who performed the abortion that the abortion was necessary to
        prevent either the death of the pregnant woman or the substantial and irreversible impairment of a major bodily
        function of the woman, where an abortion has been performed pursuant to section 3211(b)(1).</blockquote>\n
    <blockquote>\"(9) The weight of the aborted child for any abortion performed pursuant to section 3211(b)(1).
    </blockquote>\n<blockquote>\"(10) Basis for any medical judgment that a medical emergency existed which excused the
        physician from compliance with any provision of this chapter.</blockquote>\n<blockquote>\n<span
            class=\"star-pagination\">*911</span> \"(11) The information required to be reported under section 3210(a)
        (relating to determination of gestational age).</blockquote>\n<blockquote>\"(12) Whether the abortion was
        performed upon a married woman and, if so, whether notice to her spouse was given. If no notice to her spouse
        was given, the report shall also indicate the reason for failure to provide notice.</blockquote>\n<p>. . . . .
    </p>\n<p>\"(f) Report by facility.Every facility in which an abortion is performed within this Commonwealth during
        any quarter year shall file with the department a report showing the total number of abortions performed within
        the hospital or other facility during that quarter year. This report shall also show the total abortions
        performed in each trimester of pregnancy. Any report shall be available for public inspection and copying only
        if the facility receives Stateappropriated funds within the 12-calendar-month period immediately preceding the
        filing of the report. These reports shall be submitted on a form prescribed by the department which will enable
        a facility to indicate whether or not it is receiving State-appropriated funds. If the facility indicates on the
        form that it is not receiving State-appropriated funds, the department shall regard its report as confidential
        unless it receives other evidence which causes it to conclude that the facility receives State-appropriated
        funds.\"</p>\n<p>Justice Stevens, concurring in part and dissenting in part.</p>\n<p>The portions of the Court's
        opinion that I have joined are more important than those with which I disagree. I shall therefore first comment
        on significant areas of agreement, and then explain the limited character of my disagreement.</p>\n<p></p>\n<h2>
        \n<span class=\"star-pagination\">*912</span> I</h2>\n<p>The Court is unquestionably correct in concluding that
        the doctrine of <i>stare decisis</i> has controlling significance in a case of this kind, notwithstanding an
        individual Justice's concerns about the merits.<sup>[1]</sup> The central holding of <i>Roe</i> v. <i>Wade,</i>
        410 U. S. 113 (1973), has been a \"part of our law\" for almost two decades. <i>Planned Parenthood of Central
            Mo.</i> v. <i>Danforth,</i> 428 U. S. 52, 101 (1976) (Stevens, J., concurring in part and dissenting in
        part). It was a natural sequel to the protection of individual liberty established in <i>Griswold</i> v.
        <i>Connecticut,</i> 381 U. S. 479 (1965). See also <i>Carey</i> v. <i>Population Services International,</i> 431
        U. S. 678, 687, 702 (1977) (White, J., concurring in part and concurring in result). The societal costs of
        overruling <i>Roe</i> at this late date would be enormous. <i>Roe</i> is an integral part of a correct
        understanding of both the concept of liberty and the basic equality of men and women.
    </p>\n<p><i>Stare
            decisis</i> also provides a sufficient basis for my agreement with the joint opinion's reaffirmation of
        <i>Roe</i> `s postviability analysis. Specifically, I accept the proposition that \"[i]f the State is interested
        in protecting fetal life after viability, it may go so far as to proscribe abortion during that period, except
        when it is necessary to preserve the life or health of the mother.\" 410 U. S., at 163-164; see <i>ante,</i> at
        879.
    </p>\n<p>I also accept what is implicit in the Court's analysis, namely, a reaffirmation of <i>Roe</i> `s
        explanation of <i>why</i> the State's obligation to protect the life or health of the mother <span
            class=\"star-pagination\">*913</span> must take precedence over any duty to the unborn. The Court in
        <i>Roe</i> carefully considered, and rejected, the State's argument \"that the fetus is a `person' within the
        language and meaning of the Fourteenth Amendment.\" 410 U. S., at 156. After analyzing the usage of \"person\"
        in the Constitution, the Court concluded that that word \"has application only postnatally.\" <i>Id.,</i> at
        157. Commenting on the contingent property interests of the unborn that are generally represented by guardians
        ad litem, the Court noted: \"Perfection of the interests involved, again, has generally been contingent upon
        live birth. In short, the unborn have never been recognized in the law as persons in the whole sense.\"
        <i>Id.,</i> at 162. Accordingly, an abortion is not \"the termination of life entitled to Fourteenth Amendment
        protection.\" <i>Id.,</i> at 159. From this holding, there was no dissent, see <i>id.,</i> at 173; indeed, no
        Member of the Court has ever questioned this fundamental proposition. Thus, as a matter of federal
        constitutional law, a developing organism that is not yet a \"person\" does not have what is sometimes described
        as a \"right to life.\"<sup>[2]</sup> This has been and, by the Court's holding today, <span
            class=\"star-pagination\">*914</span> remains a fundamental premise of our constitutional law governing
        reproductive autonomy.
    </p>\n<p></p>\n<h2>II</h2>\n<p>My disagreement with the joint opinion begins with its
        understanding of the trimester framework established in <i>Roe.</i> Contrary to the suggestion of the joint
        opinion, <i>ante,</i> at 876, it is not a \"contradiction\" to recognize that the State may have a legitimate
        interest in potential human life and, at the same time, to conclude that that interest does not justify the
        regulation of abortion before viability (although other interests, such as maternal health, may). The fact that
        the State's interest is legitimate does not tell us when, if ever, that interest outweighs the pregnant woman's
        interest in personal liberty. It is appropriate, therefore, to consider more carefully the nature of the
        interests at stake.</p>\n<p>First, it is clear that, in order to be legitimate, the State's interest must be
        secular; consistent with the First Amendment the State may not promote a theological or sectarian interest. See
        <i>Thornburgh</i> v. <i>American College of Obstetricians and Gynecologists,</i> 476 U. S. 747, 778 (1986)
        (Stevens, J., concurring); see generally <i>Webster</i> v. <i>Reproductive Health Services,</i> 492 U. S. 490,
        563-572 (1989) (Stevens, J., concurring in part and dissenting in part). Moreover, as discussed above, the state
        interest in potential human life is not an interest <i>in loco parentis,</i> for the fetus is not a person.
    </p>
    \n<p>Identifying the State's interestswhich the States rarely articulate with any precisionmakes clear that the
        interest in protecting potential life is not grounded in the Constitution. It is, instead, an indirect interest
        supported by both humanitarian and pragmatic concerns. Many of our citizens believe that any abortion reflects
        an unacceptable disrespect for potential human life and that the performance of more <span
            class=\"star-pagination\">*915</span> than a million abortions each year is intolerable; many find
        third-trimester abortions performed when the fetus is approaching personhood particularly offensive. The State
        has a legitimate interest in minimizing such offense. The State may also have a broader interest in expanding
        the population,<sup>[3]</sup> believing society would benefit from the services of additional productive
        citizensor that the potential human lives might include the occasional Mozart or Curie. These are the kinds of
        concerns that comprise the State's interest in potential human life.</p>\n<p>In counterpoise is the woman's
        constitutional interest in liberty. One aspect of this liberty is a right to bodily integrity, a right to
        control one's person. See, <i>e. g., </i><i>Rochin</i> v. <i>California,</i> 342 U. S. 165 (1952);
        <i>Skinner</i> v. <i>Oklahoma ex rel. Williamson,</i> 316 U. S. 535 (1942). This right is neutral on the
        question of abortion: The Constitution would be equally offended by an absolute requirement that all women
        undergo abortions as by an absolute prohibition on abortions. \"Our whole constitutional heritage rebels at the
        thought of giving government the power to control men's minds.\" <i>Stanley</i> v. <i>Georgia,</i> 394 U. S.
        557, 565 (1969). The same holds true for the power to control women's bodies.
    </p>\n<p>The woman's constitutional
        liberty interest also involves her freedom to decide matters of the highest privacy and the most personal
        nature. Cf. <i>Whalen</i> v. <i>Roe,</i> 429 U. S. 589, <span class=\"star-pagination\">*916</span> 598-600
        (1977). A woman considering abortion faces \"a difficult choice having serious and personal consequences of
        major importance to her own futureperhaps to the salvation of her own immortal soul.\" <i>Thornburgh,</i> 476
        U. S., at 781. The authority to make such traumatic and yet empowering decisions is an element of basic human
        dignity. As the joint opinion so eloquently demonstrates, a woman's decision to terminate her pregnancy is
        nothing less than a matter of conscience.</p>\n<p>Weighing the State's interest in potential life and the
        woman's liberty interest, I agree with the joint opinion that the State may \"` \"expres[s] a preference for
        normal childbirth,\"` \" that the State may take steps to ensure that a woman's choice \"is thoughtful and
        informed,\" and that \"States are free to enact laws to provide a reasonable framework for a woman to make a
        decision that has such profound and lasting meaning.\" <i>Ante,</i> at 872-873. Serious questions arise,
        however, when a State attempts to \"persuade the woman to choose childbirth over abortion.\" <i>Ante,</i> at
        878. Decisional autonomy must limit the State's power to inject into a woman's most personal deliberations its
        own views of what is best. The State may promote its preferences by funding childbirth, by creating and
        maintaining alternatives to abortion, and by espousing the virtues of family; but it must respect the
        individual's freedom to make such judgments.</p>\n<p>This theme runs throughout our decisions concerning
        reproductive freedom. In general, <i>Roe</i> `s requirement that restrictions on abortions before viability be
        justified by the State's interest in <i>maternal</i> health has prevented States from interjecting regulations
        designed to influence a woman's decision. Thus, we have upheld regulations of abortion that are not efforts to
        sway or direct a woman's choice, but rather are efforts to enhance the deliberative quality of that decision or
        are neutral regulations on the health aspects of her decision. We have, for example, upheld regulations
        requiring <span class=\"star-pagination\">*917</span> written informed consent, see <i>Planned Parenthood of
            Central Mo.</i> v. <i>Danforth,</i> 428 U. S. 52 (1976); limited recordkeeping and reporting, see
        <i>ibid.;</i> and pathology reports, see <i>Planned Parenthood Assn. of Kansas City, Mo., Inc.</i> v.
        <i>Ashcroft,</i> 462 U. S. 476 (1983); as well as various licensing and qualification provisions, see, <i>e. g.,
        </i><i>Roe,</i> 410 U. S., at 150; <i>Simopoulos</i> v. <i>Virginia,</i> 462 U. S. 506 (1983). Conversely, we
        have consistently rejected state efforts to prejudice a woman's choice, either by limiting the information
        available to her, see <i>Bigelow</i> v. <i>Virginia,</i> 421 U. S. 809 (1975), or by \"requir[ing] the delivery
        of information designed `to influence the woman's informed choice between abortion or childbirth.' \"
        <i>Thornburgh,</i> 476 U. S., at 760; see also <i>Akron</i> v. <i>Akron Center for Reproductive Health,
            Inc.,</i> 462 U. S. 416, 442-449 (1983).
    </p>\n<p>In my opinion, the principles established in this long line
        of cases and the wisdom reflected in Justice Powell's opinion for the Court in <i>Akron</i> (and followed by the
        Court just six years ago in <i>Thornburgh</i> ) should govern our decision today. Under these principles, Pa.
        Cons. Stat. §§ 3205(a)(2)(i)(iii) (1990) of the Pennsylvania statute are unconstitutional. Those sections
        require a physician or counselor to provide the woman with a range of materials clearly designed to persuade her
        to choose not to undergo the abortion. While the Commonwealth is free, pursuant to § 3208 of the Pennsylvania
        law, to produce and disseminate such material, the Commonwealth may not inject such information into the woman's
        deliberations just as she is weighing such an important choice.</p>\n<p>Under this same analysis, §§
        3205(a)(1)(i) and (iii) of the Pennsylvania statute are constitutional. Those sections, which require the
        physician to inform a woman of the nature and risks of the abortion procedure and the medical risks of carrying
        to term, are neutral requirements comparable to those imposed in other medical procedures. Those sections
        indicate no effort by the Commonwealth to influence the <span class=\"star-pagination\">*918</span> woman's
        choice in any way. If anything, such requirements <i>enhance,</i> rather than skew, the woman's decisionmaking.
    </p>\n<p></p>\n<h2>III</h2>\n<p>The 24-hour waiting period required by §§ 3205(a)(1)(2) of the Pennsylvania statute
        raises even more serious concerns. Such a requirement arguably furthers the Commonwealth's interests in two
        ways, neither of which is constitutionally permissible.</p>\n<p>First, it may be argued that the 24-hour delay
        is justified by the mere fact that it is likely to reduce the number of abortions, thus furthering the
        Commonwealth's interest in potential life. But such an argument would justify any form of coercion that placed
        an obstacle in the woman's path. The Commonwealth cannot further its interests by simply wearing down the
        ability of the pregnant woman to exercise her constitutional right.</p>\n<p>Second, it can more reasonably be
        argued that the 24-hour delay furthers the Commonwealth's interest in ensuring that the woman's decision is
        informed and thoughtful. But there is no evidence that the mandated delay benefits women or that it is necessary
        to enable the physician to convey any relevant information to the patient. The mandatory delay thus appears to
        rest on outmoded and unacceptable assumptions about the decisionmaking capacity of women. While there are
        well-established and consistently maintained reasons for the Commonwealth to view with skepticism the ability of
        minors to make decisions, see <i>Hodgson</i> v. <i>Minnesota,</i> 497 U. S. 417, 449 (1990),<sup>[4]</sup> none
        of those reasons applies to an <span class=\"star-pagination\">*919</span> adult woman's decisionmaking ability.
        Just as we have left behind the belief that a woman must consult her husband before undertaking serious matters,
        see <i>ante,</i> at 895-898, so we must reject the notion that a woman is less capable of deciding matters of
        gravity. Cf. <i>Reed</i> v. <i>Reed,</i> 404 U. S. 71 (1971).</p>\n<p>In the alternative, the delay requirement
        may be premised on the belief that the decision to terminate a pregnancy is presumptively wrong. This premise is
        illegitimate. Those who disagree vehemently about the legality and morality of abortion agree about one thing:
        The decision to terminate a pregnancy is profound and difficult. No person undertakes such a decision
        lightlyand States may not presume that a woman has failed to reflect adequately merely because her conclusion
        differs from the State's preference. A woman who has, in the privacy of her thoughts and conscience, weighed the
        options and made her decision cannot be forced to reconsider all, simply because the State believes she has come
        to the wrong conclusion.<sup>[5]</sup></p>\n<p><span class=\"star-pagination\">*920</span> Part of the
        constitutional liberty to choose is the equal dignity to which each of us is entitled. A woman who decides to
        terminate her pregnancy is entitled to the same respect as a woman who decides to carry the fetus to term. The
        mandatory waiting period denies women that equal respect.</p>\n<p></p>\n<h2>IV</h2>\n<p>In my opinion, a correct
        application of the \"undue burden\" standard leads to the same conclusion concerning the constitutionality of
        these requirements. A state-imposed burden on the exercise of a constitutional right is measured both by its
        effects and by its character: A burden may be \"undue\" either because the burden is too severe or because it
        lacks a legitimate, rational justification.<sup>[6]</sup></p>\n<p>The 24-hour delay requirement fails both parts
        of this test. The findings of the District Court establish the severity of <span
            class=\"star-pagination\">*921</span> the burden that the 24-hour delay imposes on many pregnant women. Yet
        even in those cases in which the delay is not especially onerous, it is,in my opinion, \"undue\" because there
        is no evidence that such a delay serves a useful and legitimate purpose. As indicated above, there is no
        legitimate reason to require a woman who has agonized over her decision to leave the clinic or hospital and
        return again another day. While a general requirement that a physician notify her patients about the risks of a
        proposed medical procedure is appropriate, a rigid requirement that all patients wait 24 hours or (what is true
        in practice) much longer to evaluate the significance of information that is either common knowledge or
        irrelevant is an irrational and, therefore, \"undue\" burden.</p>\n<p>The counseling provisions are similarly
        infirm. Whenever government commands private citizens to speak or to listen, careful review of the justification
        for that command is particularly appropriate. In these cases, the Pennsylvania statute directs that counselors
        provide women seeking abortions with information concerning alternatives to abortion, the availability of
        medical assistance benefits, and the possibility of child-support payments. §§ 3205(a)(2)(i)(iii). The statute
        requires that this information be given to <i>all</i> women seeking abortions, including those for whom such
        information is clearly useless, such as those who are married, those who have undergone the procedure in the
        past and are fully aware of the options, and those who are fully convinced that abortion is their only
        reasonable option. Moreover, the statute requires physicians to inform all of their patients of \"[t]he probable
        gestational age of the unborn child.\" § 3205(a)(1)(ii). This information is of little decisional value in most
        cases, because 90% of all abortions are performed during the first trimester<sup>[7]</sup> when fetal age has
        less relevance than when the fetus nears viability. Nor can the information <span
            class=\"star-pagination\">*922</span> required by the statute be justified as relevant to any
        \"philosophic\" or \"social\" argument, <i>ante,</i> at 872, either favoring or disfavoring the abortion
        decision in a particular case. In light of all of these facts, I conclude that the information requirements in §
        3205(a)(1)(ii) and §§ 3205(a)(2)(i)(iii) do not serve a useful purpose and thus constitute an unnecessary and
        therefore undueburden on the woman's constitutional liberty to decide to terminate her pregnancy.</p>\n<p>
        Accordingly, while I disagree with Parts IV, VB, and VD of the joint opinion,<sup>[8]</sup> I join the
        remainder of the Court's opinion.</p>\n<p>Justice Blackmun, concurring in part, concurring in the judgment in
        part, and dissenting in part.</p>\n<p>I join Parts I, II, III, VA, VC, and VI of the joint opinion of Justices
        O'Connor, Kennedy, and Souter, <i>ante.</i> </p>\n<p>Three years ago, in <i>Webster</i> v. <i>Reproductive
            Health Services,</i> 492 U. S. 490 (1989), four Members of this Court appeared poised to \"cas[t] into
        darkness the hopes and visions of every woman in this country\" who had come to believe that the Constitution
        guaranteed her the right to reproductive choice. <i>Id.,</i> at 557 (Blackmun, J., dissenting). See <i>id.,</i>
        at 499 (plurality opinion of Rehnquist, C. J., joined by White and Kennedy, JJ.); <i>id.,</i> at 532 (Scalia,
        J., concurring in part and concurring in judgment). All that remained between the promise of <i>Roe</i> and the
        darkness of the plurality was a single, flickering flame. Decisions since <i>Webster</i> gave little reason to
        hope that this flame would cast much light. See, <i>e. g., </i><i>Ohio</i> v. <i>Akron Center for Reproductive
            Health,</i> 497 U. S. 502, 524 (1990) (Blackmun, J., dissenting). But now, just when so many expected the
        darkness to fall, the flame has grown bright.</p>\n<p><span class=\"star-pagination\">*923</span> I do not
        underestimate the significance of today's joint opinion. Yet I remain steadfast in my belief that the right to
        reproductive choice is entitled to the full protection afforded by this Court before <i>Webster.</i> And I fear
        for the darkness as four Justices anxiously await the single vote necessary to extinguish the light.</p>\n<p>
    </p>\n<h2>I</h2>\n<p>Make no mistake, the joint opinion of Justices O'Connor, Kennedy, and Souter is an act of
        personal courage and constitutional principle. In contrast to previous decisions in which Justices O'Connor and
        Kennedy postponed reconsideration of <i>Roe</i> v. <i>Wade,</i> 410 U. S. 113 (1973), the authors of the joint
        opinion today join Justice Stevens and me in concluding that \"the essential holding of <i>Roe</i> v.
        <i>Wade</i> should be retained and once again reaffirmed.\" <i>Ante,</i> at 846. In brief, five Members of this
        Court today recognize that \"the Constitution protects a woman's right to terminate her pregnancy in its early
        stages.\" <i>Ante,</i> at 844.
    </p>\n<p>A fervent view of individual liberty and the force of <i>stare
            decisis</i> have led the Court to this conclusion. <i>Ante,</i> at 853. Today a majority reaffirms that the
        Due Process Clause of the Fourteenth Amendment establishes \"a realm of personal liberty which the government
        may not enter,\" <i>ante,</i> at 847 a realm whose outer limits cannot be determined by interpretations of the
        Constitution that focus only on the specific practices of States at the time the Fourteenth Amendment was
        adopted. See <i>ante,</i> at 848-849. Included within this realm of liberty is \"`the right of the
        <i>individual,</i> married or single, to be free from unwarranted governmental intrusion into matters so
        fundamentally affecting a person as the decision whether to bear or beget a child.' \" <i>Ante,</i> at 851,
        quoting <i>Eisenstadt</i> v. <i>Baird,</i> 405 U. S. 438, 453 (1972) (emphasis in original). \"These matters,
        involving the most intimate and personal choices a person may make in a lifetime, choices central to personal
        dignity and autonomy, are <i>central</i> to the <span class=\"star-pagination\">*924</span> liberty protected by
        the Fourteenth Amendment.\" <i>Ante,</i> at 851 (emphasis added). Finally, the Court today recognizes that in
        the case of abortion, \"the liberty of the woman is at stake in a sense unique to the human condition and so
        unique to the law. The mother who carries a child to full term is subject to anxieties, to physical constraints,
        to pain that only she must bear.\" <i>Ante,</i> at 852.
    </p>\n<p>The Court's reaffirmation of <i>Roe</i> `s
        central holding is also based on the force of <i>stare decisis.</i> \"[N]o erosion of principle going to liberty
        or personal autonomy has left <i>Roe</i> `s central holding a doctrinal remnant; <i>Roe</i> portends no
        developments at odds with other precedent for the analysis of personal liberty; and no changes of fact have
        rendered viability more or less appropriate as the point at which the balance of interests tips.\" <i>Ante,</i>
        at 860-861. Indeed, the Court acknowledges that <i>Roe</i> `s limitation on state power could not be removed
        \"without serious inequity to those who have relied upon it or significant damage to the stability of the
        society governed by it.\" <i>Ante,</i> at 855. In the 19 years since <i>Roe</i> was decided, that case has
        shaped more than reproductive planning\"[a]n entire generation has come of age free to assume <i>Roe</i> `s
        concept of liberty in defining the capacity of women to act in society, and to make reproductive decisions.\"
        <i>Ante,</i> at 860. The Court understands that, having \"call[ed] the contending sides . . . to end their
        national division by accepting a common mandate rooted in the Constitution,\" <i>ante,</i> at 867, a decision to
        overrule <i>Roe</i> \"would seriously weaken the Court's capacity to exercise the judicial power and to function
        as the Supreme Court of a Nation dedicated to the rule of law.\" <i>Ante,</i> at 865. What has happened today
        should serve as a model for future Justices and a warning to all who have tried to turn this Court into yet
        another political branch.
    </p>\n<p>In striking down the Pennsylvania statute's spousal notification requirement,
        the Court has established a framework <span class=\"star-pagination\">*925</span> for evaluating abortion
        regulations that responds to the social context of women facing issues of reproductive choice.<sup>[1]</sup> In
        determining the burden imposed by the challenged regulation, the Court inquires whether the regulation's
        \"<i>purpose or effect</i> is to place a substantial obstacle in the path of a woman seeking an abortion before
        the fetus attains viability.\" <i>Ante,</i> at 878 (emphasis added). The Court reaffirms: \"The proper focus of
        constitutional inquiry is the group for whom the law is a restriction, not the group for whom the law is
        irrelevant.\" <i>Ante,</i> at 894. Looking at this group, the Court inquires, based on expert testimony,
        empirical studies, and common sense, whether \"in a large fraction of the cases in which [the restriction] is
        relevant, it will operate as a substantial obstacle to a woman's choice to undergo an abortion.\" <i>Ante,</i>
        at 895. \"A statute with this purpose is invalid because the means chosen by the State to further the interest
        in potential life must be calculated to inform the woman's free choice, not hinder it.\" <i>Ante,</i> at 877.
        And in applying its test, the Court remains sensitive to the unique role of women in the decision making
        process. Whatever may have been the practice when the Fourteenth Amendment was adopted, the Court observes,
        \"[w]omen do not lose their constitutionally protected liberty when they marry. The Constitution protects all
        individuals, male or female, married or unmarried, from the abuse of governmental power, even where that power
        is employed for the supposed benefit of a member of the individual's family.\" <i>Ante,</i> at
        898.<sup>[2]</sup></p>\n<p><span class=\"star-pagination\">*926</span> Lastly, while I believe that the joint
        opinion errs in failing to invalidate the other regulations, I am pleased that the joint opinion has not ruled
        out the possibility that these regulations may be shown to impose an unconstitutional burden. The joint opinion
        makes clear that its specific holdings are based on the insufficiency of the record before it. See, <i>e. g.,
            ante,</i> at 885-886. I am confident that in the future evidence will be produced to show that \"in a large
        fraction of the cases in which [these regulations are] relevant, [they] will operate as a substantial obstacle
        to a woman's choice to undergo an abortion.\" <i>Ante,</i> at 895.</p>\n<p></p>\n<h2>II</h2>\n<p>Today, no less
        than yesterday, the Constitution and decisions of this Court require that a State's abortion restrictions be
        subjected to the strictest judicial scrutiny. Our precedents and the joint opinion's principles require us to
        subject all non-<i>de-minimis</i> abortion regulations to strict scrutiny. Under this standard, the Pennsylvania
        statute's provisions requiring content-based counseling, a 24-hour delay, informed parental consent, and
        reporting of abortionrelated information must be invalidated.</p>\n<p></p>\n<h2>A</h2>\n<p>The Court today
        reaffirms the long recognized rights of privacy and bodily integrity. As early as 1891, the Court held, \"[n]o
        right is held more sacred, or is more carefully guarded by the common law, than the right of every individual to
        the possession and control of his own person, free from all restraint or interference of others . . . .\"
        <i>Union Pacific R. Co.</i> v. <i>Botsford,</i> 141 U. S. 250, 251 (1891). Throughout this century, this Court
        also has held that the fundamental right of privacy protects citizens against governmental intrusion <span
            class=\"star-pagination\">*927</span> in such intimate family matters as procreation, childrearing,
        marriage, and contraceptive choice. See <i>ante,</i> at 847-849. These cases embody the principle that personal
        decisions that profoundly affect bodily integrity, identity, and destiny should be largely beyond the reach of
        government. <i>Eisenstadt,</i> 405 U. S., at 453. In <i>Roe</i> v. <i>Wade</i><i>,</i> this Court correctly
        applied these principles to a woman's right to choose abortion.
    </p>\n<p>State restrictions on abortion violate a
        woman's right of privacy in two ways. First, compelled continuation of a pregnancy infringes upon a woman's
        right to bodily integrity by imposing substantial physical intrusions and significant risks of physical harm.
        During pregnancy, women experience dramatic physical changes and a wide range of health consequences. Labor and
        delivery pose additional health risks and physical demands. In short, restrictive abortion laws force women to
        endure physical invasions far more substantial than those this Court has held to violate the constitutional
        principle of bodily integrity in other contexts. See, <i>e. g., </i><i>Winston</i> v. <i>Lee,</i> 470 U. S. 753
        (1985) (invalidating surgical removal of bullet from murder suspect); <i>Rochin</i> v. <i>California,</i> 342 U.
        S. 165 (1952) (invalidating stomach pumping).<sup>[3]</sup></p>\n<p>Further, when the State restricts a woman's
        right to terminate her pregnancy, it deprives a woman of the right to make her own decision about reproduction
        and family planningcritical life choices that this Court long has deemed central to the right to privacy. The
        decision to terminate or continue a pregnancy has no less an impact on a woman's life than decisions about
        contraception or marriage. 410 U. S., <span class=\"star-pagination\">*928</span> at 153. Because motherhood has
        a dramatic impact on a woman's educational prospects, employment opportunities, and self-determination,
        restrictive abortion laws deprive her of basic control over her life. For these reasons, \"the decision whether
        or not to beget or bear a child\" lies at \"the very heart of this cluster of constitutionally protected
        choices.\" <i>Carey</i> v. <i>Population Services International,</i> 431 U. S. 678, 685 (1977).</p>\n<p>A
        State's restrictions on a woman's right to terminate her pregnancy also implicate constitutional guarantees of
        gender equality. State restrictions on abortion compel women to continue pregnancies they otherwise might
        terminate. By restricting the right to terminate pregnancies, the State conscripts women's bodies into its
        service, forcing women to continue their pregnancies, suffer the pains of childbirth, and in most instances,
        provide years of maternal care. The State does not compensate women for their services; instead, it assumes that
        they owe this duty as a matter of course. This assumptionthat women can simply be forced to accept the
        \"natural\" status and incidents of motherhoodappears to rest upon a conception of women's role that has
        triggered the protection of the Equal Protection Clause. See, <i>e. g., </i><i>Mississippi Univ. for Women</i>
        v. <i>Hogan,</i> 458 U. S. 718, 724-726 (1982); <i>Craig</i> v. <i>Boren,</i> 429 U. S. 190, 198-199
        (1976).<sup>[4]</sup> The joint opinion recognizes that these assumptions about women's place in society \"are
        no longer consistent with our <span class=\"star-pagination\">*929</span> understanding of the family, the
        individual, or the Constitution.\" <i>Ante,</i> at 897.</p>\n<p></p>\n<h2>B</h2>\n<p>The Court has held that
        limitations on the right of privacy are permissible only if they survive \"strict\" constitutional scrutinythat
        is, only if the governmental entity imposing the restriction can demonstrate that the limitation is both
        necessary and narrowly tailored to serve a compelling governmental interest. <i>Griswold</i> v.
        <i>Connecticut,</i> 381 U. S. 479, 485 (1965). We have applied this principle specifically in the context of
        abortion regulations. <i>Roe</i> v. <i>Wade,</i> 410 U. S., at 155.<sup>[5]</sup>
    </p>\n<p><i>Roe</i> implemented
        these principles through a framework that was designed \"to ensure that the woman's right to choose not become
        so subordinate to the State's interest in promoting fetal life that her choice exists in theory but not in
        fact,\" <i>ante,</i> at 872. <i>Roe</i> identified two relevant state interests: \"an interest in preserving and
        protecting the health of the pregnant woman\" and an interest in \"protecting the potentiality of human life.\"
        410 U. S., at 162. With respect to the State's interest in the health of the mother, \"the `compelling' point .
        . . is at approximately the end of the first trimester,\" because it is at that point that the mortality rate in
        abortion approaches that in childbirth. <i>Id.,</i> at 163. With respect to the State's interest in potential
        life, \"the `compelling' point is at viability,\" because it is at that point that the <span
            class=\"star-pagination\">*930</span> fetus \"presumably has the capability of meaningful life outside the
        mother's womb.\" <i>Ibid.</i> In order to fulfill the requirement of narrow tailoring, \"the State is obligated
        to make a reasonable effort to limit the effect of its regulations to the period in the trimester during which
        its health interest will be furthered.\" <i>Akron</i> v. <i>Akron Center for Reproductive Health, Inc.,</i> 462
        U. S. 416, 434 (1983).</p>\n<p>In my view, application of this analytical framework is no less warranted than
        when it was approved by seven Members of this Court in <i>Roe.</i> Strict scrutiny of state limitations on
        reproductive choice still offers the most secure protection of the woman's right to make her own reproductive
        decisions, free from state coercion. No majority of this Court has ever agreed upon an alternative approach. The
        factual premises of the trimester framework have not been undermined, see <i>Webster,</i> 492 U. S., at 553
        (Blackmun, J., dissenting), and the <i>Roe</i> framework is far more administrable, and far less manipulable,
        than the \"undue burden\" standard adopted by the joint opinion.</p>\n<p>Nonetheless, three criticisms of the
        trimester framework continue to be uttered. First, the trimester framework is attacked because its key elements
        do not appear in the text of the Constitution. My response to this attack remains the same as it was in
        <i>Webster:</i>
    </p>\n<blockquote>\"Were this a true concern, we would have to abandon most of our constitutional
        jurisprudence. [T]he `critical elements' of countless constitutional doctrines nowhere appear in the
        Constitution's text . . . . The Constitution makes no mention, for example, of the First Amendment's `actual
        malice' standard for proving certain libels, see <i>New York Times Co.</i> v. <i>Sullivan,</i> 376 U. S. 254
        (1964).. . . Similarly, the Constitution makes no mention of the rational-basis test, or the specific verbal
        formulations of intermediate and strict scrutiny by which this Court evaluates claims under the Equal Protection
        Clause. The reason is simple. Like the <i>Roe</i> framework, these <span class=\"star-pagination\">*931</span>
        tests or standards are not, and do not purport to be, rights protected by the Constitution. Rather, they are
        judge-made methods for evaluating and measuring the strength and scope of constitutional rights or for balancing
        the constitutional rights of individuals against the competing interests of government.\" <i>Id.,</i> at 548.
    </blockquote>\n<p>The second criticism is that the framework more closely resembles a regulatory code than a body of
        constitutional doctrine. Again, my answer remains the same as in <i>Webster:</i></p>\n<blockquote>\"[I]f this
        were a true and genuine concern, we would have to abandon vast areas of our constitutional jurisprudence. . . .
        Are [the distinctions entailed in the trimester framework] any finer, or more `regulatory,' than the
        distinctions we have often drawn in our First Amendment jurisprudence, where, for example, we have held that a
        `release time' program permitting publicschool students to leave school grounds during school hours to receive
        religious instruction does not violate the Establishment Clause, even though a release-time program permitting
        religious instruction on school grounds does violate the Clause? Compare <i>Zorach</i> v. <i>Clauson,</i> 343 U.
        S. 306 (1952), with <i>Illinois ex rel. Mc-</i> <i>Collum</i> v. <i>Board of Education of School Dist. No.
            71,</i> <i>Champaign County,</i> 333 U. S. 203 (1948). . . . Similarly, in a Sixth Amendment case, the Court
        held that although an overnight ban on attorney-client communication violated the constitutionally guaranteed
        right to counsel, <i>Geders</i> v. <i>United States,</i> 425 U. S. 80 (1976), that right was not violated when a
        trial judge separated a defendant from his lawyer during a 15-minute recess after the defendant's direct
        testimony. <i>Perry</i> v. <i>Leeke,</i> 488 U. S. 272 (1989).</blockquote>\n<blockquote>\"That numerous
        constitutional doctrines result in narrow differentiations between similar circumstances does <span
            class=\"star-pagination\">*932</span> not mean that this Court has abandoned adjudication in favor of
        regulation.\" <i>Id.,</i> at 549-550.</blockquote>\n<p>The final, and more genuine, criticism of the trimester
        framework is that it fails to find the State's interest in potential human life compelling throughout pregnancy.
        No Member of this Courtnor for that matter, the Solicitor General, see Tr. of Oral Arg. 42has ever questioned
        our holding in <i>Roe</i> that an abortion is not \"the termination of life entitled to Fourteenth Amendment
        protection.\" 410 U. S., at 159. Accordingly, a State's interest in protecting fetal life is not grounded in the
        Constitution. Nor, consistent with our Establishment Clause, can it be a theological or sectarian interest. See
        <i>Thornburgh</i> v. <i>American College of Obstetricians and Gynecologists,</i> 476 U. S. 747, 778 (1986)
        (Stevens, J., concurring). It is, instead, a legitimate interest grounded in humanitarian or pragmatic concerns.
        See <i>ante,</i> at 914-915 (Stevens, J., concurring in part and dissenting in part).
    </p>\n<p>But while a State
        has \"legitimate interests from the outset of the pregnancy in protecting the health of the woman and the life
        of the fetus that may become a child,\" <i>ante,</i> at 846, legitimate interests are not enough. To overcome
        the burden of strict scrutiny, the interests must be compelling. The question then is how best to accommodate
        the State's interest in potential human life with the constitutional liberties of pregnant women. Again, I stand
        by the views I expressed in <i>Webster:</i></p>\n<blockquote>\"I remain convinced, as six other Members of this
        Court 16 years ago were convinced, that the <i>Roe</i> framework, and the viability standard in particular,
        fairly, sensibly, and effectively functions to safeguard the constitutional liberties of pregnant women while
        recognizing and accommodating the State's interest in potential human life. The viability line reflects the
        biological facts and truths of fetal development; it marks that threshold moment prior to which a fetus cannot
        survive separate from the <span class=\"star-pagination\">*933</span> woman and cannot reasonably and
        objectively be regarded as a subject of rights or interests distinct from, or paramount to, those of the
        pregnant woman. At the same time, the viability standard takes account of the undeniable fact that as the fetus
        evolves into its postnatal form, and as it loses its dependence on the uterine environment, the State's interest
        in the fetus' potential human life, and in fostering a regard for human life in general, becomes compelling. As
        a practical matter, because viability follows `quickening'the point at which a woman feels movement in her
        womband because viability occurs no earlier than 23 weeks gestational age, it establishes an easily applicable
        standard for regulating abortion while providing a pregnant woman ample time to exercise her fundamental right
        with her responsible physician to terminate her pregnancy.\" 492 U. S., at 553-554.<sup>[6]</sup></blockquote>\n
    <p><i>Roe</i>`s trimester framework does not ignore the State's interest in prenatal life. Like Justice Stevens,
        <i>ante,</i> at 916, I agree that the State may take steps to ensure that a woman's choice \"is thoughtful and
        informed,\" <i>ante,</i> at 872, and that \"States are free to enact laws to provide a reasonable framework for
        a woman to make a decision that has such profound and lasting meaning.\" <i>Ante,</i> at 873. But
    </p>\n
    <blockquote>\"[s]erious questions arise . . . when a State attempts to persuade the woman to choose childbirth over
        abortion. <i>Ante,</i> at 878. Decisional autonomy must limit the State's power to inject into a woman's most
        personal deliberations its own views of what is best. The State may promote its preferences by funding
        childbirth, by creating and maintaining alternatives to abortion, and by espousing the virtues of family; but it
        must respect <span class=\"star-pagination\">*934</span> the individual's freedom to make such judgments.\"
        <i>Ante,</i> at 916 (Stevens, J., concurring in part and dissenting in part) (internal quotation marks omitted).
    </blockquote>\n<p>As the joint opinion recognizes, \"the means chosen by the State to further the interest in
        potential life must be calculated to inform the woman's free choice, not hinder it.\" <i>Ante,</i> at 877.</p>\n
    <p>In sum, <i>Roe</i> `s requirement of strict scrutiny as implemented through a trimester framework should not be
        disturbed. No other approach has gained a majority, and no other is more protective of the woman's fundamental
        right. Lastly, no other approach properly accommodates the woman's constitutional right with the State's
        legitimate interests.</p>\n<p></p>\n<h2>C</h2>\n<p>Application of the strict scrutiny standard results in the
        invalidation of all the challenged provisions. Indeed, as this Court has invalidated virtually identical
        provisions in prior cases, <i>stare decisis</i> requires that we again strike them down.</p>\n<p>This Court has
        upheld informed- and written-consent requirements only where the State has demonstrated that they genuinely
        further important health-related state concerns. See <i>Planned Parenthood of Central Mo.</i> v.
        <i>Danforth,</i> 428 U. S. 52, 65-67 (1976). A State may not, under the guise of securing informed consent,
        \"require the delivery of information `designed to influence the woman's informed choice between abortion or
        childbirth.' \" <i>Thornburgh,</i> 476 U. S., at 760, quoting <i>Akron,</i> 462 U. S., at 443-444. Rigid
        requirements that a specific body of information be imparted to a woman in all cases, regardless of the needs of
        the patient, improperly intrude upon the discretion of the pregnant woman's physician and thereby impose an
        \"`undesired and uncomfortable straitjacket.' \" <i>Thornburgh,</i> 476 U. S., at 762, quoting <i>Danforth,</i>
        428 U. S., at 67, n. 8.
    </p>\n<p>Measured against these principles, some aspects of the Pennsylvania
        informed-consent scheme are unconstitutional. <span class=\"star-pagination\">*935</span> While it is
        unobjectionable for the Commonwealth to require that the patient be informed of the nature of the procedure, the
        health risks of the abortion and of childbirth, and the probable gestational age of the unborn child, compare
        Pa. Cons. Stat. §§ 3205(a)(i)-(iii) (1990) with <i>Akron,</i> 462 U. S., at 446, n. 37, I remain unconvinced
        that there is a vital state need for insisting that the information be provided by a physician rather than a
        counselor. <i>Id.,</i> at 448. The District Court found that the physician-only requirement necessarily would
        increase costs to the plaintiff clinics, costs that undoubtedly would be passed on to patients. And because
        trained women counselors are often more understanding than physicians, and generally have more time to spend
        with patients, see App. 366-387, the physician-only disclosure requirement is not narrowly tailored to serve the
        Commonwealth's interest in protecting maternal health.</p>\n<p>Sections 3205(a)(2)(i)-(iii) of the Act further
        requires that the physician or a qualified nonphysician inform the woman that printed materials are available
        from the Commonwealth that describe the fetus and provide information about medical assistance for childbirth,
        information about child support from the father, and a list of agencies offering adoption and other services as
        alternatives to abortion. <i>Thornburgh</i> invalidated biased patient-counseling requirements virtually
        identical to the one at issue here. What we said of those requirements fully applies in these cases:</p>\n
    <blockquote>\"[T]he listing of agencies in the printed Pennsylvania form presents serious problems; it contains
        names of agencies that well may be out of step with the needs of the particular woman and thus places the
        physician in an awkward position and infringes upon his or her professional responsibilities. Forcing the
        physician or counselor to present the materials and the list to the woman makes him or her in effect an agent of
        the State in treating the woman and places his or her imprimatur upon both the materials and the list. All this
        is, or <span class=\"star-pagination\">*936</span> comes close to being, state medicine imposed upon the woman,
        not the professional medical guidance she seeks, and it officially structuresas it obviously was intended to
        dothe dialogue between the woman and her physician.</blockquote>\n<blockquote>\"The requirements . . . that the
        woman be advised that medical assistance benefits may be available, and that the father is responsible for
        financial assistance in the support of the child similarly are poorly disguised elements of discouragement for
        the abortion decision. Much of this . . . , for many patients, would be irrelevant and inappropriate. For a
        patient with a life-threatening pregnancy, the `information' in its very rendition may be cruel as well as
        destructive of the physician-patient relationship. As any experienced social worker or other counselor knows,
        theoretical financial responsibility often does not equate with fulfillment . . . . Under the guise of informed
        consent, the Act requires the dissemination of information that is not relevant to such consent, and, thus, it
        advances no legitimate state interest.\" 476 U. S., at 762-763 (citation omitted).</blockquote>\n<p>\"This type
        of compelled information is the antithesis of informed consent,\" <i>id.,</i> at 764, and goes far beyond merely
        describing the general subject matter relevant to the woman's decision. \"That the Commonwealth does not, and
        surely would not, compel similar disclosure of every possible peril of necessary surgery or of simple
        vaccination, reveals the anti-abortion character of the statute and its real purpose.\"
        <i>Ibid.</i><sup>[7]</sup>
    </p>\n<p><span class=\"star-pagination\">*937</span> The 24-hour waiting period
        following the provision of the foregoing information is also clearly unconstitutional. The District Court found
        that the mandatory 24-hour delay could lead to delays in excess of 24 hours, thus increasing health risks, and
        that it would require two visits to the abortion provider, thereby increasing travel time, exposure to further
        harassment, and financial cost. Finally, the District Court found that the requirement would pose especially
        significant burdens on women living in rural areas and those women that have difficulty explaining their
        whereabouts. 744 F. Supp. 1323, 1378-1379 (ED Pa. 1990). In <i>Akron</i> this Court invalidated a similarly
        arbitrary or inflexible waiting period because, as here, it furthered no legitimate state
        interest.<sup>[8]</sup></p>\n<p>As Justice Stevens insightfully concludes, the mandatory delay rests either on
        outmoded or unacceptable assumptions about the decision making capacity of women or the belief that the decision
        to terminate the pregnancy is <span class=\"star-pagination\">*938</span> presumptively wrong. <i>Ante,</i> at
        918-919. The requirement that women consider this obvious and slanted information for an additional 24 hours
        contained in these provisions will only influence the woman's decision in improper ways. The vast majority of
        women will know this informationof the few that do not, it is less likely that their minds will be changed by
        this information than it will be either by the realization that the State opposes their choice or the need once
        again to endure abuse and harassment on return to the clinic.<sup>[9]</sup></p>\n<p>Except in the case of a
        medical emergency, § 3206 requires a physician to obtain the informed consent of a parent or guardian before
        performing an abortion on an unemancipated minor or an incompetent woman. Based on evidence in the record, the
        District Court concluded that, in order to fulfill the informed-consent requirement, generally accepted medical
        principles would require an in-person visit by the parent to the facility. 744 F. Supp., at 1382. Although the
        Court \"has recognized that the State has somewhat broader authority to regulate the activities of children than
        of adults,\" the State nevertheless must demonstrate that there is a \"<i>significant state interest</i> in
        conditioning an abortion . . . that is not present in the case of an adult.\" <i>Danforth,</i> 428 U. S., at
        74-75 (emphasis added). The requirement of an inperson visit would carry with it the risk of a delay of several
        days or possibly weeks, even where the parent is willing to consent. While the State has an interest in
        encouraging parental involvement in the minor's abortion decision, § 3206 is not narrowly drawn to serve that
        interest.<sup>[10]</sup></p>\n<p><span class=\"star-pagination\">*939</span> Finally, the Pennsylvania statute
        requires every facility performing abortions to report its activities to the Commonwealth. Pennsylvania contends
        that this requirement is valid under <i>Danforth,</i> in which this Court held that recordkeeping and reporting
        requirements that are reasonably directed to the preservation of maternal health and that properly respect a
        patient's confidentiality are permissible. <i>Id.,</i> at 79-81. The Commonwealth attempts to justify its
        required reports on the ground that the public has a right to know how its tax dollars are spent. A regulation
        designed to inform the public about public expenditures does not further the Commonwealth's interest in
        protecting maternal health. Accordingly, such a regulation cannot justify a legally significant burden on a
        woman's right to obtain an abortion.</p>\n<p>The confidential reports concerning the identities and medical
        judgment of physicians involved in abortions at first glance may seem valid, given the Commonwealth's interest
        in maternal health and enforcement of the Act. The District Court found, however, that, notwithstanding the
        confidentiality protections, many physicians, particularly those who have previously discontinued performing
        abortions because of harassment, would refuse to refer patients to abortion clinics if their names were to
        appear on these reports. 744 F. Supp., at 1392. The Commonwealth has failed to show that the name of the
        referring physician either adds to the pool of scientific knowledge concerning abortion or is reasonably related
        to the Commonwealth's interest in maternal health. I therefore agree with the District Court's conclusion that
        the confidential reporting requirements are unconstitutional <span class=\"star-pagination\">*940</span> insofar
        as they require the name of the referring physician and the basis for his or her medical judgment.</p>\n<p>In
        sum, I would affirm the judgment in No. 91-902 and reverse the judgment in No. 91-744 and remand the cases for
        further proceedings.</p>\n<p></p>\n<h2>III</h2>\n<p>At long last, The Chief Justice and those who have joined
        him admit it. Gone are the contentions that the issue need not be (or has not been) considered. There, on the
        first page, for all to see, is what was expected: \"We believe that <i>Roe</i> was wrongly decided, and that it
        can and should be overruled consistently with our traditional approach to <i>stare decisis</i> in constitutional
        cases.\" <i>Post,</i> at 944. If there is much reason to applaud the advances made by the joint opinion today,
        there is far more to fear from The Chief Justice's opinion.</p>\n<p>The Chief Justice's criticism of <i>Roe</i>
        follows from his stunted conception of individual liberty. While recognizing that the Due Process Clause
        protects more than simple physical liberty, he then goes on to construe this Court's personalliberty cases as
        establishing only a laundry list of particular rights, rather than a principled account of how these particular
        rights are grounded in a more general right of privacy. <i>Post,</i> at 951. This constricted view is reinforced
        by The Chief Justice's exclusive reliance on tradition as a source of fundamental rights. He argues that the
        record in favor of a right to abortion is no stronger than the record in <i>Michael H.</i> v. <i>Gerald D.,</i>
        491 U. S. 110 (1989), where the plurality found no fundamental right to visitation privileges by an adulterous
        father, or in <i>Bowers</i> v. <i>Hardwick,</i> 478 U. S. 186 (1986), where the Court found no fundamental right
        to engage in homosexual sodomy, or in a case involving the \"`firing [of] a gun . . . into another person's
        body.' \" <i>Post,</i> at 951-952. In The Chief Justice's world, a woman considering whether to terminate a
        pregnancy is entitled to no more protection than adulterers, murderers, and so-called sexual <span
            class=\"star-pagination\">*941</span> deviates.<sup>[11]</sup> Given The Chief Justice's exclusive reliance
        on tradition, people using contraceptives seem the next likely candidate for his list of outcasts.</p>\n<p>Even
        more shocking than The Chief Justice's cramped notion of individual liberty is his complete omission of any
        discussion of the effects that compelled childbirth and motherhood have on women's lives. The only expression of
        concern with women's health is purely instrumentalfor The Chief Justice, only women's <i>psychological</i>
        health is a concern, and only to the extent that he assumes that every woman who decides to have an abortion
        does so without serious consideration of the moral implications of her decision. <i>Post,</i> at 967-968. In
        short, The Chief Justice's view of the State's compelling interest in maternal health has less to do with health
        than it does with compelling women to be maternal.</p>\n<p>Nor does The Chief Justice give any serious
        consideration to the doctrine of <i>stare decisis.</i> For The Chief Justice, the facts that gave rise to
        <i>Roe</i> are surprisingly simple: \"women become pregnant, there is a point somewhere, depending on medical
        technology, where a fetus becomes viable, and women give birth to children.\" <i>Post,</i> at 955. This
        characterization of the issue thus allows The Chief Justice quickly to discard the joint opinion's reliance
        argument by asserting that \"reproductive planning could take virtually immediate account of\" a decision
        overruling <i>Roe. Post,</i> at 956 (internal quotation marks omitted).
    </p>\n<p>The Chief Justice's narrow
        conception of individual liberty and <i>stare decisis</i> leads him to propose the same standard of review
        proposed by the plurality in <i>Webster.</i> \"States may regulate abortion procedures in ways rationally
        related to a legitimate state interest. <i>Williamson</i> v. <i>Lee Optical of Oklahoma, Inc.,</i> 348 U. S.
        483, 491 (1955); cf. <i>Stanley</i> v. <i>Illinois,</i> 405 U. S. 645, 651-653 (1972).\" <i>Post,</i> at 966.
        The <span class=\"star-pagination\">*942</span> Chief Justice then further weakens the test by providing an
        insurmountable requirement for facial challenges: Petitioners must \"`show that no set of circumstances exists
        under which the [provision] would be valid.' \" <i>Post,</i> at 973, quoting <i>Ohio</i> v. <i>Akron Center for
            Reproductive Health,</i> 497 U. S., at 514. In short, in his view, petitioners must prove that the statute
        cannot constitutionally be applied to <i>anyone.</i> Finally, in applying his standard to the
        spousal-notification provision, The Chief Justice contends that the record lacks any \"hard evidence\" to
        support the joint opinion's contention that a \"large fraction\" of women who prefer not to notify their
        husbands involve situations of battered women and unreported spousal assault. <i>Post,</i> at 974, n. 2. Yet
        throughout the explication of his standard, The Chief Justice never explains what hard evidence is, how large a
        fraction is required, or how a battered woman is supposed to pursue an as-applied challenge.</p>\n<p>Under his
        standard, States can ban abortion if that ban is rationally related to a legitimate state interesta standard
        which the United States calls \"deferential, but not toothless.\" Yet when pressed at oral argument to describe
        the teeth, the best protection that the Solicitor General could offer to women was that a prohibition, enforced
        by criminal penalties, <i>with no exception for the life of the mother,</i> \"could raise very serious
        questions.\" Tr. of Oral Arg. 48. Perhaps, the Solicitor General offered, the failure to include an exemption
        for the life of the mother would be \"arbitrary and capricious.\" <i>Id.,</i> at 49. If, as The Chief Justice
        contends, the undue burden test is made out of whole cloth, the so-called \"arbitrary and capricious\" limit is
        the Solicitor General's \"new clothes.\"</p>\n<p>Even if it is somehow \"irrational\" for a State to require a
        woman to risk her life for her child, what protection is offered for women who become pregnant through rape or
        incest? Is there anything arbitrary or capricious about a <span class=\"star-pagination\">*943</span> State's
        prohibiting the sins of the father from being visited upon his offspring?<sup>[12]</sup></p>\n<p>But, we are
        reassured, there is always the protection of the democratic process. While there is much to be praised about our
        democracy, our country since its founding has recognized that there are certain fundamental liberties that are
        not to be left to the whims of an election. A woman's right to reproductive choice is one of those fundamental
        liberties. Accordingly, that liberty need not seek refuge at the ballot box.</p>\n<p></p>\n<h2>IV</h2>\n<p>In
        one sense, the Court's approach is worlds apart from that of The Chief Justice and Justice Scalia. And yet, in
        another sense, the distance between the two approaches is shortthe distance is but a single vote.</p>\n<p>I am
        83 years old. I cannot remain on this Court forever, and when I do step down, the confirmation process for my
        successor well may focus on the issue before us today. That, I regret, may be exactly where the choice between
        the two worlds will be made.</p>\n<p><span class=\"star-pagination\">*944</span> Chief Justice Rehnquist, with
        whom Justice White, Justice Scalia, and Justice Thomas join, concurring in the judgment in part and dissenting
        in part.</p>\n<p>The joint opinion, following its newly minted variation on <i>stare decisis,</i> retains the
        outer shell of <i>Roe</i> v. <i>Wade,</i> 410 U. S. 113 (1973), but beats a wholesale retreat from the substance
        of that case. We believe that <i>Roe</i> was wrongly decided, and that it can and should be overruled
        consistently with our traditional approach to <i>stare decisis</i> in constitutional cases. We would adopt the
        approach of the plurality in <i>Webster</i> v. <i>Reproductive Health Services,</i> 492 U. S. 490 (1989), and
        uphold the challenged provisions of the Pennsylvania statute in their entirety.</p>\n<p></p>\n<h2>I</h2>\n<p>In
        ruling on this litigation below, the Court of Appeals for the Third Circuit first observed that \"this appeal
        does not directly implicate <i>Roe;</i> this case involves the regulation of abortions rather than their
        outright prohibition.\" 947 F. 2d 682, 687 (1991). Accordingly, the court directed its attention to the question
        of the standard of review for abortion regulations. In attempting to settle on the correct standard, however,
        the court confronted the confused state of this Court's abortion jurisprudence. After considering the several
        opinions in <i>Webster</i> v. <i>Reproductive Health Services, supra</i><i>,</i> and <i>Hodgson</i> v.
        <i>Minnesota,</i> 497 U. S. 417 (1990), the Court of Appeals concluded that Justice O'Connor's \"undue burden\"
        test was controlling, as that was the narrowest ground on which we had upheld recent abortion regulations. 947
        F. 2d, at 693-697 (\"When a fragmented court decides a case and no single rationale explaining the result enjoys
        the assent of five Justices, the holding of the Court may be viewed as that position taken by those Members who
        concurred in the judgments on the narrowest grounds\" (quoting <i>Marks</i> v. <i>United States,</i> 430 U. S.
        188, 193 (1977) (internal quotation marks omitted))). Applying this standard, the Court of Appeals upheld all of
        the challenged regulations except the one <span class=\"star-pagination\">*945</span> requiring a woman to
        notify her spouse of an intended abortion.
    </p>\n<p>In arguing that this Court should invalidate each of the
        provisions at issue, petitioners insist that we reaffirm our decision in <i>Roe</i> v. <i>Wade,
            supra</i><i>,</i> in which we held unconstitutional a Texas statute making it a crime to procure an abortion
        except to save the life of the mother.<sup>[1]</sup> We agree with the Court of Appeals that our decision in
        <i>Roe</i> is not directly implicated by the Pennsylvania statute, which does not prohibit, but simply
        regulates, abortion. But, as the Court of Appeals found, the state of our post-<i>Roe</i> decisional law dealing
        with the regulation of abortion is confusing and uncertain, indicating that a reexamination of that line of
        cases is in order. Unfortunately for those who must apply this Court's decisions, the reexamination undertaken
        today leaves the Court no less divided than beforehand. Although they reject the trimester framework that formed
        the underpinning of <i>Roe,</i> Justices O'Connor, Kennedy, and Souter adopt a revised undue burden standard to
        analyze the challenged regulations. We conclude, however, that such an outcome is an unjustified constitutional
        compromise, one which leaves the Court in a position to closely scrutinize all types of abortion regulations
        despite the fact that it lacks the power to do so under the Constitution.
    </p>\n<p>In <i>Roe,</i> the Court
        opined that the State \"does have an important and legitimate interest in preserving and protecting the health
        of the pregnant woman, . . . and that it has still another important and legitimate interest in protecting <span
            class=\"star-pagination\">*946</span> the potentiality of human life.\" 410 U. S., at 162 (emphasis
        omitted). In the companion case of <i>Doe</i> v. <i>Bolton,</i> 410 U. S. 179 (1973), the Court referred to its
        conclusion in <i>Roe</i> \"that a pregnant woman does not have an absolute constitutional right to an abortion
        on her demand.\" 410 U. S., at 189. But while the language and holdings of these cases appeared to leave States
        free to regulate abortion procedures in a variety of ways, later decisions based on them have found considerably
        less latitude for such regulations than might have been expected.</p>\n<p>For example, after <i>Roe,</i> many
        States have sought to protect their young citizens by requiring that a minor seeking an abortion involve her
        parents in the decision. Some States have simply required notification of the parents, while others have
        required a minor to obtain the consent of her parents. In a number of decisions, however, the Court has
        substantially limited the States in their ability to impose such requirements. With regard to parental
        <i>notice</i> requirements, we initially held that a State could require a minor to notify her parents before
        proceeding with an abortion. <i>H. L.</i> v. <i>Matheson,</i> 450 U. S. 398, 407-410 (1981). Recently, however,
        we indicated that a State's ability to impose a notice requirement actually depends on whether it requires
        notice of one or both parents. We concluded that although the Constitution might allow a State to demand that
        notice be given to one parent prior to an abortion, it may not require that similar notice be given to
        <i>two</i> parents, unless the State incorporates a judicial bypass procedure in that two-parent requirement.
        <i>Hodgson</i> v. <i>Minnesota, supra</i><i>.</i>
    </p>\n<p>We have treated parental <i>consent</i> provisions
        even more harshly. Three years after <i>Roe,</i> we invalidated a Missouri regulation requiring that an
        unmarried woman under the age of 18 obtain the consent of one of her parents before proceeding with an abortion.
        We held that our abortion jurisprudence prohibited the State from imposing such a \"blanket provision. . .
        requiring the consent of a parent.\" <i>Planned Parenthood</i> <span class=\"star-pagination\">*947</span> <i>of
            Central Mo.</i> v. <i>Danforth,</i> 428 U. S. 52, 74 (1976). In <i>Bellotti</i> v. <i>Baird,</i> 443 U. S.
        622 (1979), the Court struck down a similar Massachusetts parental consent statute. A majority of the Court
        indicated, however, that a State could constitutionally require parental consent, if it alternatively allowed a
        pregnant minor to obtain an abortion without parental consent by showing either that she was mature enough to
        make her own decision, or that the abortion would be in her best interests. See <i>id.,</i> at 643-644
        (plurality opinion); <i>id.,</i> at 656-657 (White, J., dissenting). In light of <i>Bellotti,</i> we have upheld
        one parental consent regulation which incorporated a judicial bypass option we viewed as sufficient, see
        <i>Planned Parenthood Assn. of Kansas City, Mo., Inc.</i> v. <i>Ashcroft,</i> 462 U. S. 476 (1983), but have
        invalidated another because of our belief that the judicial procedure did not satisfy the dictates of
        <i>Bellotti,</i> see <i>Akron</i> v. <i>Akron Center for Reproductive Health, Inc.,</i> 462 U. S. 416, 439-442
        (1983). We have never had occasion, as we have in the parental notice context, to further parse our parental
        consent jurisprudence into oneparent and two-parent components.
    </p>\n<p>In <i>Roe,</i> the Court observed that
        certain States recognized the right of the father to participate in the abortion decision in certain
        circumstances. Because neither <i>Roe</i> nor <i>Doe</i> involved the assertion of any paternal right, the Court
        expressly stated that the case did not disturb the validity of regulations that protected such a right.
        <i>Roe</i> v. <i>Wade, supra,</i> at 165, n. 67. But three years later, in <i>Danforth,</i> the Court extended
        its abortion jurisprudence and held that a State could not require that a woman obtain the consent of her spouse
        before proceeding with an abortion. <i>Planned Parenthood of Central Mo.</i> v. <i>Danforth,</i> 428 U. S., at
        69-71.
    </p>\n<p>States have also regularly tried to ensure that a woman's decision to have an abortion is an
        informed and wellconsidered one. In <i>Danforth,</i> we upheld a requirement that a woman sign a consent form
        prior to her abortion, and observed that \"it is desirable and imperative that [the decision] <span
            class=\"star-pagination\">*948</span> be made with full knowledge of its nature and consequences.\"
        <i>Id.,</i> at 67. Since that case, however, we have twice invalidated state statutes designed to impart such
        knowledge to a woman seeking an abortion. In <i>Akron,</i> we held unconstitutional a regulation requiring a
        physician to inform a woman seeking an abortion of the status of her pregnancy, the development of her fetus,
        the date of possible viability, the complications that could result from an abortion, and the availability of
        agencies providing assistance and information with respect to adoption and childbirth. <i>Akron</i> v. <i>Akron
            Center for Reproductive Health, supra,</i> at 442-445. More recently, in <i>Thornburgh</i> v. <i>American
            College of Obstetricians and Gynecologists,</i> 476 U. S. 747 (1986), we struck down a more limited
        Pennsylvania regulation requiring that a woman be informed of the risks associated with the abortion procedure
        and the assistance available to her if she decided to proceed with her pregnancy, because we saw the compelled
        information as \"the antithesis of informed consent.\" <i>Id.,</i> at 764. Even when a State has sought only to
        provide information that, in our view, was consistent with the <i>Roe</i> framework, we concluded that the State
        could not require that a physician furnish the information, but instead had to alternatively allow nonphysician
        counselors to provide it. <i>Akron</i> v. <i>Akron Center for Reproductive Health,</i> 462 U. S., at 448-449. In
        <i>Akron</i> as well, we went further and held that a State may not require a physician to wait 24 hours to
        perform an abortion after receiving the consent of a woman. Although the State sought to ensure that the woman's
        decision was carefully considered, the Court concluded that the Constitution forbade the State to impose any
        sort of delay. <i>Id.,</i> at 449-451.
    </p>\n<p>We have not allowed States much leeway to regulate even the
        actual abortion procedure. Although a State can require that second-trimester abortions be performed in
        outpatient clinics, see <i>Simopoulos</i> v. <i>Virginia,</i> 462 U. S. 506 (1983), we concluded in <i>Akron</i>
        and <i>Ashcroft</i> that a State could not <span class=\"star-pagination\">*949</span> require that such
        abortions be performed only in hospitals. See <i>Akron</i> v. <i>Akron Center for Reproductive Health,
            supra,</i> at 437-439; <i>Planned Parenthood Assn. of Kansas City, Mo., Inc.</i> v. <i>Ashcroft, supra,</i>
        at 481-482. Despite the fact that <i>Roe</i> expressly allowed regulation after the first trimester in
        furtherance of maternal health, \"`present medical knowledge,' \" in our view, could not justify such a
        hospitalization requirement under the trimester framework. <i>Akron</i> v. <i>Akron Center for Reproductive
            Health, supra,</i> at 437 (quoting <i>Roe</i> v. <i>Wade, supra,</i> at 163). And in <i>Danforth,</i> the
        Court held that Missouri could not outlaw the saline amniocentesis method of abortion, concluding that the
        Missouri Legislature had \"failed to appreciate and to consider several significant facts\" in making its
        decision. 428 U. S., at 77.</p>\n<p>Although <i>Roe</i> allowed state regulation after the point of viability to
        protect the potential life of the fetus, the Court subsequently rejected attempts to regulate in this manner. In
        <i>Colautti</i> v. <i>Franklin,</i> 439 U. S. 379 (1979), the Court struck down a statute that governed the
        determination of viability. <i>Id.,</i> at 390-397. In the process, we made clear that the trimester framework
        incorporated only one definition of viabilityoursas we forbade States to decide that a certain objective
        indicator\"be it weeks of gestation or fetal weight or any other single factor\"should govern the definition
        of viability. <i>Id.,</i> at 389. In that same case, we also invalidated a regulation requiring a physician to
        use the abortion technique offering the best chance for fetal survival when performing postviability abortions.
        See <i>id.,</i> at 397-401; see also <i>Thornburgh</i> v. <i>American College of Obstetricians and
            Gynecologists,</i> 476 U. S., at 768-769 (invalidating a similar regulation). In <i>Thornburgh,</i> the
        Court struck down Pennsylvania's requirement that a second physician be present at post viability abortions to
        help preserve the health of the unborn child, on the ground that it did not incorporate a sufficient medical
        emergency exception. <i>Id.,</i> at 769-771. Regulations governing the treatment of aborted fetuses have <span
            class=\"star-pagination\">*950</span> met a similar fate. In <i>Akron,</i> we invalidated a provision
        requiring physicians performing abortions to \"insure that the remains of the unborn child are disposed of in a
        humane and sanitary manner.\" 462 U. S., at 451 (internal quotation marks omitted).
    </p>\n<p>Dissents in these
        cases expressed the view that the Court was expanding upon <i>Roe</i> in imposing ever greater restrictions on
        the States. See <i>Thornburgh</i> v. <i>American College of Obstetricians and Gynecologists,</i> 476 U. S., at
        783 (Burger, C. J., dissenting) (\"The extent to which the Court has departed from the limitations expressed in
        <i>Roe</i> is readily apparent\"); <i>id.,</i> at 814 (White, J., dissenting) (\"[T]he majority indiscriminately
        strikes down statutory provisions that in no way contravene the right recognized in <i>Roe</i> \"). And, when
        confronted with state regulations of this type in past years, the Court has become increasingly more divided:
        The three most recent abortion cases have not commanded a Court opinion. See <i>Ohio</i> v. <i>Akron Center for
            Reproductive Health,</i> 497 U. S. 502 (1990); <i>Hodgson</i> v. <i>Minnesota,</i> 497 U. S. 417 (1990);
        <i>Webster</i> v. <i>Reproductive Health Services,</i> 492 U. S. 490 (1989).
    </p>\n<p>The task of the Court of
        Appeals in the present cases was obviously complicated by this confusion and uncertainty. Following <i>Marks</i>
        v. <i>United States,</i> 430 U. S. 188 (1977), it concluded that in light of <i>Webster</i> and <i>Hodgson,</i>
        the strict scrutiny standard enunciated in <i>Roe</i> was no longer applicable, and that the \"undue burden\"
        standard adopted by Justice O'Connor was the governing principle. This state of confusion and disagreement
        warrants reexamination of the \"fundamental right\" accorded to a woman's decision to abort a fetus in
        <i>Roe,</i> with its concomitant requirement that any state regulation of abortion survive \"strict scrutiny.\"
        See <i>Payne</i> v. <i>Tennessee,</i> 501 U. S. 808, 827-828 (1991) (observing that reexamination of
        constitutional decisions is appropriate when those decisions have generated uncertainty and failed to provide
        clear guidance, because \"correction through legislative <span class=\"star-pagination\">*951</span> action is
        practically impossible\" (internal quotation marks omitted)); <i>Garcia</i> v. <i>San Antonio Metropolitan
            Transit Authority,</i> 469 U. S. 528, 546-547, 557 (1985).
    </p>\n<p>We have held that a liberty interest
        protected under the Due Process Clause of the Fourteenth Amendment will be deemed fundamental if it is
        \"implicit in the concept of ordered liberty.\" <i>Palko</i> v. <i>Connecticut,</i> 302 U. S. 319, 325 (1937).
        Three years earlier, in <i>Snyder</i> v. <i>Massachusetts,</i> 291 U. S. 97 (1934), we referred to a \"principle
        of justice so rooted in the traditions and conscience of our people as to be ranked as fundamental.\"
        <i>Id.,</i> at 105; see also <i>Michael H.</i> v. <i>Gerald D.,</i> 491 U. S. 110, 122 (1989) (plurality
        opinion) (citing the language from <i>Snyder</i>). These expressions are admittedly not precise, but our
        decisions implementing this notion of \"fundamental\" rights do not afford any more elaborate basis on which to
        base such a classification.
    </p>\n<p>In construing the phrase \"liberty\" incorporated in the Due Process Clause
        of the Fourteenth Amendment, we have recognized that its meaning extends beyond freedom from physical restraint.
        In <i>Pierce</i> v. <i>Society of Sisters,</i> 268 U. S. 510 (1925), we held that it included a parent's right
        to send a child to private school; in <i>Meyer</i> v. <i>Nebraska,</i> 262 U. S. 390 (1923), we held that it
        included a right to teach a foreign language in a parochial school. Building on these cases, we have held that
        the term \"liberty\" includes a right to marry, <i>Loving</i> v. <i>Virginia,</i> 388 U. S. 1 (1967); a right to
        procreate, <i>Skinner</i> v. <i>Oklahoma ex rel. Williamson,</i> 316 U. S. 535 (1942); and a right to use
        contraceptives, <i>Griswold</i> v. <i>Connecticut,</i> 381 U. S. 479 (1965); <i>Eisenstadt</i> v. <i>Baird,</i>
        405 U. S. 438 (1972). But a reading of these opinions makes clear that they do not endorse any all-encompassing
        \"right of privacy.\"</p>\n<p>In <i>Roe</i> v. <i>Wade</i><i>,</i> the Court recognized a \"guarantee of
        personal privacy\" which \"is broad enough to encompass a woman's decision whether or not to terminate her
        pregnancy.\" 410 U. S., at 152-153. We are now of the view that, in terming this right fundamental, the Court in
        <i>Roe</i> read the earlier <span class=\"star-pagination\">*952</span> opinions upon which it based its
        decision much too broadly. Unlike marriage, procreation, and contraception, abortion \"involves the purposeful
        termination of a potential life.\" <i>Harris</i> v. <i>McRae,</i> 448 U. S. 297, 325 (1980). The abortion
        decision must therefore \"be recognized as <i>sui generis,</i> different in kind from the others that the Court
        has protected under the rubric of personal or family privacy and autonomy.\" <i>Thornburgh</i> v. <i>American
            College of Obstetricians and Gynecologists, supra,</i> at 792 (White, J., dissenting). One cannot ignore the
        fact that a woman is not isolated in her pregnancy, and that the decision to abort necessarily involves the
        destruction of a fetus. See <i>Michael H.</i> v. <i>Gerald D., supra,</i> at 124, n. 4 (To look \"at the act
        which is assertedly the subject of a liberty interest in isolation from its effect upon other people [is] like
        inquiring whether there is a liberty interest in firing a gun where the case at hand happens to involve its
        discharge into another person's body\").
    </p>\n<p>Nor do the historical traditions of the American people support
        the view that the right to terminate one's pregnancy is \"fundamental.\" The common law which we inherited from
        England made abortion after \"quickening\" an offense. At the time of the adoption of the Fourteenth Amendment,
        statutory prohibitions or restrictions on abortion were commonplace; in 1868, at least 28 of the then-37 States
        and 8 Territories had statutes banning or limiting abortion. J. Mohr, Abortion in America 200 (1978). By the
        turn of the century virtually every State had a law prohibiting or restricting abortion on its books. By the
        middle of the present century, a liberalization trend had set in. But 21 of the restrictive abortion laws in
        effect in 1868 were still in effect in 1973 when <i>Roe</i> was decided, and an overwhelming majority of the
        States prohibited abortion unless necessary to preserve the life or health of the mother. <i>Roe</i> v.
        <i>Wade,</i> 410 U. S., at 139-140; <i>id.,</i> at 176-177, n. 2 (Rehnquist, J., dissenting). On this record, it
        can scarcely be said that any deeply rooted tradition of relatively unrestricted abortion in our history <span
            class=\"star-pagination\">*953</span> supported the classification of the right to abortion as
        \"fundamental\" under the Due Process Clause of the Fourteenth Amendment.
    </p>\n<p>We think, therefore, both in
        view of this history and of our decided cases dealing with substantive liberty under the Due Process Clause,
        that the Court was mistaken in <i>Roe</i> when it classified a woman's decision to terminate her pregnancy as a
        \"fundamental right\" that could be abridged only in a manner which withstood \"strict scrutiny.\" In so
        concluding, we repeat the observation made in <i>Bowers</i> v. <i>Hardwick,</i> 478 U. S. 186 (1986):</p>\n
    <blockquote>\"Nor are we inclined to take a more expansive view of our authority to discover new fundamental rights
        imbedded in the Due Process Clause. The Court is most vulnerable and comes nearest to illegitimacy when it deals
        with judge-made constitutional law having little or no cognizable roots in the language or design of the
        Constitution.\" <i>Id.,</i> at 194.</blockquote>\n<p>We believe that the sort of constitutionally imposed
        abortion code of the type illustrated by our decisions following <i>Roe</i> is inconsistent \"with the notion of
        a Constitution cast in general terms, as ours is, and usually speaking in general principles, as ours does.\"
        <i>Webster</i> v. <i>Reproductive Health Services,</i> 492 U. S., at 518 (plurality opinion). The Court in
        <i>Roe</i> reached too far when it analogized the right to abort a fetus to the rights involved in <i>Pierce,
            Meyer, Loving,</i> and <i>Griswold,</i> and thereby deemed the right to abortion fundamental.
    </p>\n<p></p>\n
    <h2>II</h2>\n<p>The joint opinion of Justices O'Connor, Kennedy, and Souter cannot bring itself to say that
        <i>Roe</i> was correct as an original matter, but the authors are of the view that \"the immediate question is
        not the soundness of <i>Roe</i> `s resolution of the issue, but the precedential force that must be accorded to
        its holding.\" <i>Ante,</i> at 871. Instead of claiming that <i>Roe</i> <span
            class=\"star-pagination\">*954</span> was correct as a matter of original constitutional interpretation, the
        opinion therefore contains an elaborate discussion of <i>stare decisis.</i> This discussion of the principle of
        <i>stare decisis</i> appears to be almost entirely dicta, because the joint opinion does not apply that
        principle in dealing with <i>Roe. Roe</i> decided that a woman had a fundamental right to an abortion. The joint
        opinion rejects that view. <i>Roe</i> decided that abortion regulations were to be subjected to \"strict
        scrutiny\" and could be justified only in the light of \"compelling state interests.\" The joint opinion rejects
        that view. <i>Ante,</i> at 872-873; see <i>Roe</i> v. <i>Wade, supra,</i> at 162-164. <i>Roe</i> analyzed
        abortion regulation under a rigid trimester framework, a framework which has guided this Court's decision making
        for 19 years. The joint opinion rejects that framework. <i>Ante,</i> at 873.
    </p>\n<p><i>Stare decisis</i> is
        defined in Black's Law Dictionary as meaning \"to abide by, or adhere to, decided cases.\" Black's Law
        Dictionary 1406 (6th ed. 1990). Whatever the \"central holding\" of <i>Roe</i> that is left after the joint
        opinion finishes dissecting it is surely not the result of that principle. While purporting to adhere to
        precedent, the joint opinion instead revises it. <i>Roe</i> continues to exist, but only in the way a storefront
        on a western movie set exists: a mere facade to give the illusion of reality. Decisions following <i>Roe,</i>
        such as <i>Akron</i> v. <i>Akron Center for Reproductive Health, Inc.,</i> 462 U. S. 416 (1983), and
        <i>Thornburgh</i> v. <i>American College of Obstetricians and Gynecologists,</i> 476 U. S. 747 (1986), are
        frankly overruled in part under the \"undue burden\" standard expounded in the joint opinion. <i>Ante,</i> at
        881-884.
    </p>\n<p>In our view, authentic principles of <i>stare decisis</i> do not require that any portion of
        the reasoning in <i>Roe</i> be kept intact. \"<i>Stare decisis</i> is not . . . a universal, inexorable
        command,\" especially in cases involving the interpretation of the Federal Constitution. <i>Burnet</i> v.
        <i>Coronado Oil &amp; Gas Co.,</i> 285 U. S. 393, 405 (1932) (Brandeis, J., dissenting). Erroneous decisions in
        such constitutional cases are uniquely durable, because correction through legislative action, save for <span
            class=\"star-pagination\">*955</span> constitutional amendment, is impossible. It is therefore our duty to
        reconsider constitutional interpretations that \"depar[t] from a proper understanding\" of the Constitution.
        <i>Garcia</i> v. <i>San Antonio Metropolitan Transit Authority,</i> 469 U. S., at 557; see <i>United States</i>
        v. <i>Scott,</i> 437 U. S. 82, 101 (1978) (\"`[I]n cases involving the Federal Constitution, . . . [t]he Court
        bows to the lessons of experience and the force of better reasoning, recognizing that the process of trial and
        error, so fruitful in the physical sciences, is appropriate also in the judicial function'\" (quoting
        <i>Burnet</i> v. <i>Coronado Oil &amp; Gas Co., supra,</i> at 406-408 (Brandeis, J., dissenting))); <i>Smith</i>
        v. <i>Allwright,</i> 321 U. S. 649, 665 (1944). Our constitutional watch does not cease merely because we have
        spoken before on an issue; when it becomes clear that a prior constitutional interpretation is unsound we are
        obliged to reexamine the question. See, <i>e. g., </i><i>West Virginia Bd. of Ed.</i> v. <i>Barnette,</i> 319 U.
        S. 624, 642 (1943); <i>Erie R. Co.</i> v. <i>Tompkins,</i> 304 U. S. 64, 74-78 (1938).
    </p>\n<p>The joint opinion
        discusses several <i>stare decisis</i> factors which, it asserts, point toward retaining a portion of
        <i>Roe.</i> Two of these factors are that the main \"factual underpinning\" of <i>Roe</i> has remained the same,
        and that its doctrinal foundation is no weaker now than it was in 1973. <i>Ante,</i> at 857-860. Of course, what
        might be called the basic facts which gave rise to <i>Roe</i> have remained the samewomen become pregnant,
        there is a point somewhere, depending on medical technology, where a fetus becomes viable, and women give birth
        to children. But this is only to say that the same facts which gave rise to <i>Roe</i> will continue to give
        rise to similar cases. It is not a reason, in and of itself, why those cases must be decided in the same
        incorrect manner as was the first case to deal with the question. And surely there is no requirement, in
        considering whether to depart from <i>stare decisis</i> in a constitutional case, that a decision be more wrong
        now than it was at the time it was rendered. If that were true, the most outlandish constitutional decision
        could survive <span class=\"star-pagination\">*956</span> forever, based simply on the fact that it was no more
        outlandish later than it was when originally rendered.
    </p>\n<p>Nor does the joint opinion faithfully follow this
        alleged requirement. The opinion frankly concludes that <i>Roe</i> and its progeny were wrong in failing to
        recognize that the State's interests in maternal health and in the protection of unborn human life exist
        throughout pregnancy. <i>Ante,</i> at 871-873. But there is no indication that these components of <i>Roe</i>
        are any more incorrect at this juncture than they were at its inception.</p>\n<p>The joint opinion also points
        to the reliance interests involved in this context in its effort to explain why precedent must be followed for
        precedent's sake. Certainly it is true that where reliance is truly at issue, as in the case of judicial
        decisions that have formed the basis for private decisions, \"[c]onsiderations in favor of <i>stare decisis</i>
        are at their acme.\" <i>Payne</i> v. <i>Tennessee,</i> 501 U. S., at 828. But, as the joint opinion apparently
        agrees, <i>ante,</i> at 855-856, any traditional notion of reliance is not applicable here. The Court today cuts
        back on the protection afforded by <i>Roe,</i> and no one claims that this action defeats any reliance interest
        in the disavowed trimester framework. Similarly, reliance interests would not be diminished were the Court to go
        further and acknowledge the full error of <i>Roe,</i> as \"reproductive planning could take virtually immediate
        account of\" this action. <i>Ante,</i> at 856.</p>\n<p>The joint opinion thus turns to what can only be
        described as an unconventionaland unconvincingnotion of reliance, a view based on the surmise that the
        availability of abortion since <i>Roe</i> has led to \"two decades of economic and social developments\" that
        would be undercut if the error of <i>Roe</i> were recognized. <i>Ante,</i> at 856. The joint opinion's assertion
        of this fact is undeveloped and totally conclusory. In fact, one cannot be sure to what economic and social
        developments the opinion is referring. Surely it is dubious to suggest that women have reached their \"places in
        society\" in <span class=\"star-pagination\">*957</span> reliance upon <i>Roe,</i> rather than as a result of
        their determination to obtain higher education and compete with men in the job market, and of society's
        increasing recognition of their ability to fill positions that were previously thought to be reserved only for
        men. <i>Ante,</i> at 856.</p>\n<p>In the end, having failed to put forth any evidence to prove any true
        reliance, the joint opinion's argument is based solely on generalized assertions about the national psyche, on a
        belief that the people of this country have grown accustomed to the <i>Roe</i> decision over the last 19 years
        and have \"ordered their thinking and living around\" it. <i>Ante,</i> at 856. As an initial matter, one might
        inquire how the joint opinion can view the \"central holding\" of <i>Roe</i> as so deeply rooted in our
        constitutional culture, when it so casually uproots and disposes of that same decision's trimester framework.
        Furthermore, at various points in the past, the same could have been said about this Court's erroneous decisions
        that the Constitution allowed \"separate but equal\" treatment of minorities, see <i>Plessy</i> v.
        <i>Ferguson,</i> 163 U. S. 537 (1896), or that \"liberty\" under the Due Process Clause protected \"freedom of
        contract,\" see <i>Adkins</i> v. <i>Children's Hospital of District of Columbia,</i> 261 U. S. 525 (1923);
        <i>Lochner</i> v. <i>New York,</i> 198 U. S. 45 (1905). The \"separate but equal\" doctrine lasted 58 years
        after <i>Plessy,</i> and <i>Lochner</i> `s protection of contractual freedom lasted 32 years. However, the
        simple fact that a generation or more had grown used to these major decisions did not prevent the Court from
        correcting its errors in those cases, nor should it prevent us from correctly interpreting the Constitution
        here. See <i>Brown</i> v. <i>Board of Education,</i> 347 U. S. 483 (1954) (rejecting the \"separate but equal\"
        doctrine); <i>West Coast Hotel Co.</i> v. <i>Parrish,</i> 300 U. S. 379 (1937) (overruling <i>Adkins</i> v.
        <i>Children's Hospital, supra,</i> in upholding Washington's minimum wage law).
    </p>\n<p>Apparently realizing
        that conventional <i>stare decisis</i> principles do not support its position, the joint opinion advances a
        belief that retaining a portion of <i>Roe</i> is necessary to protect <span
            class=\"star-pagination\">*958</span> the \"legitimacy\" of this Court. <i>Ante,</i> at 861-869. Because the
        Court must take care to render decisions \"grounded truly in principle,\" and not simply as political and social
        compromises, <i>ante,</i> at 865, the joint opinion properly declares it to be this Court's duty to ignore the
        public criticism and protest that may arise as a result of a decision. Few would quarrel with this statement,
        although it may be doubted that Members of this Court, holding their tenure as they do during constitutional
        \"good behavior,\" are at all likely to be intimidated by such public protests.</p>\n<p>But the joint opinion
        goes on to state that when the Court \"resolve[s] the sort of intensely divisive controversy reflected in
        <i>Roe</i> and those rare, comparable cases,\" its decision is exempt from reconsideration under established
        principles of <i>stare decisis</i> in constitutional cases. <i>Ante,</i> at 866. This is so, the joint opinion
        contends, because in those \"intensely divisive\" cases the Court has \"call[ed] the contending sides of a
        national controversy to end their national division by accepting a common mandate rooted in the Constitution,\"
        and must therefore take special care not to be perceived as \"surrender[ing] to political pressure\" and
        continued opposition. <i>Ante,</i> at 866, 867. This is a truly novel principle, one which is contrary to both
        the Court's historical practice and to the Court's traditional willingness to tolerate criticism of its
        opinions. Under this principle, when the Court has ruled on a divisive issue, it is apparently prevented from
        overruling that decision for the sole reason that it was incorrect, <i>unless opposition to the original
            decision has died away.</i>
    </p>\n<p>The first difficulty with this principle lies in its assumption that
        cases that are \"intensely divisive\" can be readily distinguished from those that are not. The question of
        whether a particular issue is \"intensely divisive\" enough to qualify for special protection is entirely
        subjective and dependent on the individual assumptions of the Members of this Court. In addition, because the
        Court's duty is to ignore public opinion and criticism on issues that come before it, its Members are <span
            class=\"star-pagination\">*959</span> in perhaps the worst position to judge whether a decision divides the
        Nation deeply enough to justify such uncommon protection. Although many of the Court's decisions divide the
        populace to a large degree, we have not previously on that account shied away from applying normal rules of
        <i>stare decisis</i> when urged to reconsider earlier decisions. Over the past 21 years, for example, the Court
        has overruled in whole or in part 34 of its previous constitutional decisions. See <i>Payne</i> v. <i>Tennessee,
            supra,</i> at 828-830, and n. 1 (listing cases).
    </p>\n<p>The joint opinion picks out and discusses two prior
        Court rulings that it believes are of the \"intensely divisive\" variety, and concludes that they are of
        comparable dimension to <i>Roe. Ante,</i> at 861-864 (discussing <i>Lochner</i> v. <i>New York,
            supra</i><i>,</i> and <i>Plessy</i> v. <i>Ferguson, supra</i> ). It appears to us very odd indeed that the
        joint opinion chooses as benchmarks two cases in which the Court chose <i>not</i> to adhere to erroneous
        constitutional precedent, but instead enhanced its stature by acknowledging and correcting its error, apparently
        in violation of the joint opinion's \"legitimacy\" principle. See <i>West Coast Hotel Co.</i> v. <i>Parrish,
            supra</i><i>; </i><i>Brown</i> v. <i>Board of Education, supra</i><i>.</i> One might also wonder how it is
        that the joint opinion puts these, and not others, in the \"intensely divisive\" category, and how it assumes
        that these are the only two lines of cases of comparable dimension to <i>Roe.</i> There is no reason to think
        that either <i>Plessy</i> or <i>Lochner</i> produced the sort of public protest when they were decided that
        <i>Roe</i> did. There were undoubtedly large segments of the bench and bar who agreed with the dissenting views
        in those cases, but surely that cannot be what the Court means when it uses the term \"intensely divisive,\" or
        many other cases would have to be added to the list. In terms of public protest, however, <i>Roe,</i> so far as
        we know, was unique. But just as the Court should not respond to that sort of protest by retreating from the
        decision simply to allay the concerns of the protesters, it should likewise not respond by determining to adhere
        to the <span class=\"star-pagination\">*960</span> decision at all costs lest it <i>seem</i> to be retreating
        under fire. Public protests should not alter the normal application of <i>stare decisis,</i> lest perfectly
        lawful protest activity be penalized by the Court itself.
    </p>\n<p>Taking the joint opinion on its own terms, we
        doubt that its distinction between <i>Roe,</i> on the one hand, and <i>Plessy</i> and <i>Lochner,</i> on the
        other, withstands analysis. The joint opinion acknowledges that the Court improved its stature by overruling
        <i>Plessy</i> in <i>Brown</i> on a deeply divisive issue. And our decision in <i>West Coast Hotel,</i> which
        overruled <i>Adkins</i> v. <i>Children's Hospital, supra,</i> and <i>Lochner,</i> was rendered at a time when
        Congress was considering President Franklin Roosevelt's proposal to \"reorganize\" this Court and enable him to
        name six additional Justices in the event that any Member of the Court over the age of 70 did not elect to
        retire. It is difficult to imagine a situation in which the Court would face more intense opposition to a prior
        ruling than it did at that time, and, under the general principle proclaimed in the joint opinion, the Court
        seemingly should have responded to this opposition by stubbornly refusing to reexamine the <i>Lochner</i>
        rationale, lest it lose legitimacy by appearing to \"overrule under fire.\" <i>Ante,</i> at 867.
    </p>\n<p>The
        joint opinion agrees that the Court's stature would have been seriously damaged if in <i>Brown</i> and <i>West
            Coast Hotel</i> it had dug in its heels and refused to apply normal principles of <i>stare decisis</i> to
        the earlier decisions. But the opinion contends that the Court was entitled to overrule <i>Plessy</i> and
        <i>Lochner</i> in those cases, despite the existence of opposition to the original decisions, only because both
        the Nation and the Court had learned new lessons in the interim. This is at best a feebly supported, <i>post
            hoc</i> rationalization for those decisions.
    </p>\n<p>For example, the opinion asserts that the Court could
        justifiably overrule its decision in <i>Lochner</i> only because the Depression had convinced \"most people\"
        that constitutional protection of contractual freedom contributed to an economy <span
            class=\"star-pagination\">*961</span> that failed to protect the welfare of all. <i>Ante,</i> at 861. Surely
        the joint opinion does not mean to suggest that people saw this Court's failure to uphold minimum wage statutes
        as the cause of the Great Depression! In any event, the <i>Lochner</i> Court did not base its rule upon the
        policy judgment that an unregulated market was fundamental to a stable economy; it simple believed, erroneously,
        that \"liberty\" under the Due Process Clause protected the \"right to make a contract.\" <i>Lochner</i> v.
        <i>New York,</i> 198 U. S., at 53. Nor is it the case that the people of this Nation only discovered the dangers
        of extreme laissez-faire economics because of the Depression. State laws regulating maximum hours and minimum
        wages were in existence well before that time. A Utah statute of that sort enacted in 1896 was involved in our
        decision in <i>Holden</i> v. <i>Hardy,</i> 169 U. S. 366 (1898), and other States followed suit shortly
        afterwards, see, <i>e. g., </i><i>Muller</i> v. <i>Oregon,</i> 208 U. S. 412 (1908); <i>Bunting</i> v.
        <i>Oregon,</i> 243 U. S. 426 (1917). These statutes were indeed enacted because of a belief on the part of their
        sponsors that \"freedom of contract\" did not protect the welfare of workers, demonstrating that that belief
        manifested itself more than a generation before the Great Depression. Whether \"most people\" had come to share
        it in the hard times of the 1930's is, insofar as anything the joint opinion advances, entirely speculative. The
        crucial failing at that time was not that workers were not paid a fair wage, but that there was no work
        available at <i>any</i> wage.
    </p>\n<p>When the Court finally recognized its error in <i>West Coast Hotel,</i> it
        did not engage in the <i>post hoc</i> rationalization that the joint opinion attributes to it today; it did not
        state that <i>Lochner</i> had been based on an economic view that had fallen into disfavor, and that it
        therefore should be overruled. Chief Justice Hughes in his opinion for the Court simply recognized what Justice
        Holmes had previously recognized in his <i>Lochner</i> dissent, that \"[t]he Constitution does not speak of
        freedom of contract.\" <i>West Coast Hotel Co.</i> v. <i>Parrish,</i> 300 U. S., at 391; <i>Lochner</i> v.
        <i>New York, supra,</i> at 75 (Holmes, <span class=\"star-pagination\">*962</span> J., dissenting) (\"[A]
        constitution is not intended to embody a particular economic theory, whether of paternalism and the organic
        relation of the citizen to the State or of <i>laissez faire</i> \"). Although the Court did acknowledge in the
        last paragraph of its opinion the state of affairs during the thencurrent Depression, the theme of the opinion
        is that the Court had been mistaken as a matter of constitutional law when it embraced \"freedom of contract\"
        32 years previously.
    </p>\n<p>The joint opinion also agrees that the Court acted properly in rejecting the
        doctrine of \"separate but equal\" in <i>Brown.</i> In fact, the opinion lauds <i>Brown</i> in comparing it to
        <i>Roe. Ante,</i> at 867. This is strange, in that under the opinion's \"legitimacy\" principle the Court would
        seemingly have been forced to adhere to its erroneous decision in <i>Plessy</i> because of its \"intensely
        divisive\" character. To us, adherence to <i>Roe</i> today under the guise of \"legitimacy\" would seem to
        resemble more closely adherence to <i>Plessy</i> on the same ground. Fortunately, the Court did not choose that
        option in <i>Brown,</i> and instead frankly repudiated <i>Plessy.</i> The joint opinion concludes that such
        repudiation was justified only because of newly discovered evidence that segregation had the effect of treating
        one race as inferior to another. But it can hardly be argued that this was not urged upon those who decided
        <i>Plessy,</i> as Justice Harlan observed in his dissent that the law at issue \"puts the brand of servitude and
        degradation upon a large class of our fellow-citizens, our equals before the law.\" <i>Plessy</i> v.
        <i>Ferguson,</i> 163 U. S., at 562. It is clear that the same arguments made before the Court in <i>Brown</i>
        were made in <i>Plessy</i> as well. The Court in <i>Brown</i> simply recognized, as Justice Harlan had
        recognized beforehand, that the Fourteenth Amendment does not permit racial segregation. The rule of
        <i>Brown</i> is not tied to popular opinion about the evils of segregation; it is a judgment that the Equal
        Protection Clause does not permit racial segregation, no matter whether the public might come to believe that it
        is beneficial. On that ground it stands, and on that ground <span class=\"star-pagination\">*963</span> alone
        the Court was justified in properly concluding that the <i>Plessy</i> Court had erred.
    </p>\n<p>There is also a
        suggestion in the joint opinion that the propriety of overruling a \"divisive\" decision depends in part on
        whether \"most people\" would now agree that it should be overruled. Either the demise of opposition or its
        progression to substantial popular agreement apparently is required to allow the Court to reconsider a divisive
        decision. How such agreement would be ascertained, short of a public opinion poll, the joint opinion does not
        say. But surely even the suggestion is totally at war with the idea of \"legitimacy\" in whose name it is
        invoked. The Judicial Branch derives its legitimacy, not from following public opinion, but from deciding by its
        best lights whether legislative enactments of the popular branches of Government comport with the Constitution.
        The doctrine of <i>stare decisis</i> is an adjunct of this duty, and should be no more subject to the vagaries
        of public opinion than is the basic judicial task.</p>\n<p>There are other reasons why the joint opinion's
        discussion of legitimacy is unconvincing as well. In assuming that the Court is perceived as \"surrender[ing] to
        political pressure\" when it overrules a controversial decision, <i>ante,</i> at 867, the joint opinion forgets
        that there are two sides to any controversy. The joint opinion asserts that, in order to protect its legitimacy,
        the Court must refrain from overruling a controversial decision lest it be viewed as favoring those who oppose
        the decision. But a decision to <i>adhere</i> to prior precedent is subject to the same criticism, for in such a
        case one can easily argue that the Court is responding to those who have demonstrated in favor of the original
        decision. The decision in <i>Roe</i> has engendered large demonstrations, including repeated marches on this
        Court and on Congress, both in opposition to and in support of that opinion. A decision either way on <i>Roe</i>
        can therefore be perceived as favoring one group or the other. But this perceived dilemma arises only if one
        assumes, as the joint opinion does, that the Court <span class=\"star-pagination\">*964</span> should make its
        decisions with a view toward speculative public perceptions. If one assumes instead, as the Court surely did in
        both <i>Brown</i> and <i>West Coast Hotel,</i> that the Court's legitimacy is enhanced by faithful
        interpretation of the Constitution irrespective of public opposition, such selfengendered difficulties may be
        put to one side.</p>\n<p><i>Roe</i> is not this Court's only decision to generate conflict. Our decisions in
        some recent capital cases, and in <i>Bowers</i> v. <i>Hardwick,</i> 478 U. S. 186 (1986), have also engendered
        demonstrations in opposition. The joint opinion's message to such protesters appears to be that they must cease
        their activities in order to serve their cause, because their protests will only cement in place a decision
        which by normal standards of <i>stare decisis</i> should be reconsidered. Nearly a century ago, Justice David J.
        Brewer of this Court, in an article discussing criticism of its decisions, observed that \"many criticisms may
        be, like their authors, devoid of good taste, but better all sorts of criticism than no criticism at all.\"
        Justice Brewer on \"The Nation's Anchor,\" 57 Albany L. J. 166, 169 (1898). This was good advice to the Court
        then, as it is today. Strong and often misguided criticism of a decision should not render the decision immune
        from reconsideration, lest a fetish for legitimacy penalize freedom of expression.</p>\n<p>The end result of the
        joint opinion's paeans of praise for legitimacy is the enunciation of a brand new standard for evaluating state
        regulation of a woman's right to abortion the \"undue burden\" standard. As indicated above, <i>Roe</i> v.
        <i>Wade</i> adopted a \"fundamental right\" standard under which state regulations could survive only if they
        met the requirement of \"strict scrutiny.\" While we disagree with that standard, it at least had a recognized
        basis in constitutional law at the time <i>Roe</i> was decided. The same cannot be said for the \"undue burden\"
        standard, which is created largely out of whole cloth by the authors of the joint opinion. It is a standard
        which even today does not command the support of a majority of this Court. And it will not, we believe, result
        <span class=\"star-pagination\">*965</span> in the sort of \"simple limitation,\" easily applied, which the
        joint opinion anticipates. <i>Ante,</i> at 855. In sum, it is a standard which is not built to last.
    </p>\n<p>In
        evaluating abortion regulations under that standard, judges will have to decide whether they place a
        \"substantial obstacle\" in the path of a woman seeking an abortion. <i>Ante,</i> at 877. In that this standard
        is based even more on a judge's subjective determinations than was the trimester framework, the standard will do
        nothing to prevent \"judges from roaming at large in the constitutional field\" guided only by their personal
        views. <i>Griswold</i> v. <i>Connecticut,</i> 381 U. S., at 502 (Harlan, J., concurring in judgment). Because
        the undue burden standard is plucked from nowhere, the question of what is a \"substantial obstacle\" to
        abortion will undoubtedly engender a variety of conflicting views. For example, in the very matter before us
        now, the authors of the joint opinion would uphold Pennsylvania's 24-hour waiting period, concluding that a
        \"particular burden\" on some women is not a substantial obstacle. <i>Ante,</i> at 887. But the authors would at
        the same time strike down Pennsylvania's spousal notice provision, after finding that in a \"large fraction\" of
        cases the provision will be a substantial obstacle. <i>Ante,</i> at 895. And, while the authors conclude that
        the informed consent provisions do not constitute an \"undue burden,\" Justice Stevens would hold that they do.
        <i>Ante,</i> at 920-922.
    </p>\n<p>Furthermore, while striking down the spousal <i>notice</i> regulation, the
        joint opinion would uphold a parental <i>consent</i> restriction that certainly places very substantial
        obstacles in the path of a minor's abortion choice. The joint opinion is forthright in admitting that it draws
        this distinction based on a policy judgment that parents will have the best interests of their children at
        heart, while the same is not necessarily true of husbands as to their wives. <i>Ante,</i> at 895. This may or
        may not be a correct judgment, but it is quintessentially a legislative one. The \"undue burden\" inquiry does
        not in any way supply the distinction between parental consent and <span class=\"star-pagination\">*966</span>
        spousal consent which the joint opinion adopts. Despite the efforts of the joint opinion, the undue burden
        standard presents nothing more workable than the trimester framework which it discards today. Under the guise of
        the Constitution, this Court will still impart its own preferences on the States in the form of a complex
        abortion code.</p>\n<p>The sum of the joint opinion's labors in the name of <i>stare decisis</i> and
        \"legitimacy\" is this: <i>Roe</i> v. <i>Wade</i> stands as a sort of judicial Potemkin Village, which may be
        pointed out to passers-by as a monument to the importance of adhering to precedent. But behind the facade, an
        entirely new method of analysis, without any roots in constitutional law, is imported to decide the
        constitutionality of state laws regulating abortion. Neither <i>stare decisis</i> nor \"legitimacy\" are truly
        served by such an effort.</p>\n<p>We have stated above our belief that the Constitution does not subject state
        abortion regulations to heightened scrutiny. Accordingly, we think that the correct analysis is that set forth
        by the plurality opinion in <i>Webster.</i> A woman's interest in having an abortion is a form of liberty
        protected by the Due Process Clause, but States may regulate abortion procedures in ways rationally related to a
        legitimate state interest. <i>Williamson</i> v. <i>Lee Optical of Oklahoma, Inc.,</i> 348 U. S. 483, 491 (1955);
        cf. <i>Stanley</i> v. <i>Illinois,</i> 405 U. S. 645, 651-653 (1972). With this rule in mind, we examine each of
        the challenged provisions.</p>\n<p></p>\n<h2>III</h2>\n<p></p>\n<h2>A</h2>\n<p>Section 3205 of the Act imposes
        certain requirements related to the informed consent of a woman seeking an abortion. 18 Pa. Cons. Stat. § 3205
        (1990). Section 3205(a)(1) requires that the referring or performing physician must inform a woman contemplating
        an abortion of (i) the nature of the procedure and the risks and alternatives that a reasonable patient would
        find material; (ii) the fetus' probable gestational <span class=\"star-pagination\">*967</span> age; and (iii)
        the medical risks involved in carrying her pregnancy to term. Section 3205(a)(2) requires a physician or a
        nonphysician counselor to inform the woman that (i) the state health department publishes free materials
        describing the fetus at different stages and listing abortion alternatives; (ii) medical assistance benefits may
        be available for prenatal, childbirth, and neonatal care; and (iii) the child's father is liable for child
        support. The Act also imposes a 24-hour waiting period between the time that the woman receives the required
        information and the time that the physician is allowed to perform the abortion. See Appendix to opinion of
        O'Connor, Kennedy, and Souter, JJ., <i>ante,</i> at 902-904.</p>\n<p>This Court has held that it is certainly
        within the province of the States to require a woman's voluntary and informed consent to an abortion. See
        <i>Thornburgh</i> v. <i>American College of Obstetricians and Gynecologists,</i> 476 U. S., at 760. Here,
        Pennsylvania seeks to further its legitimate interest in obtaining informed consent by ensuring that each woman
        \"is aware not only of the reasons for having an abortion, but also of the risks associated with an abortion and
        the availability of assistance that might make the alternative of normal childbirth more attractive than it
        might otherwise appear.\" <i>Id.,</i> at 798-799 (White, J., dissenting).
    </p>\n<p>We conclude that this
        provision of the statute is rationally related to the State's interest in assuring that a woman's consent to an
        abortion be a fully informed decision.</p>\n<p>Section 3205(a)(1) requires a physician to disclose certain
        information about the abortion procedure and its risks and alternatives. This requirement is certainly no large
        burden, as the Court of Appeals found that \"the record shows that the clinics, without exception, insist on
        providing this information to women before an abortion is performed.\" 947 F. 2d, at 703. We are of the view
        that this information \"clearly is related to maternal health and to the State's legitimate purpose in requiring
        informed consent.\" <i>Akron</i> v. <span class=\"star-pagination\">*968</span> <i>Akron Center for Reproductive
            Health, Inc.,</i> 462 U. S., at 446. An accurate description of the gestational age of the fetus and of the
        risks involved in carrying a child to term helps to further both those interests and the State's legitimate
        interest in unborn human life. See <i>id.,</i> at 445-446, n. 37 (required disclosure of gestational age of the
        fetus \"certainly is not objectionable\"). Although petitioners contend that it is unreasonable for the State to
        require that a physician, as opposed to a nonphysician counselor, disclose this information, we agree with the
        Court of Appeals that a State \"may rationally decide that physicians are better qualified than counselors to
        impart this information and answer questions about the medical aspects of the available alternatives.\" 947 F.
        2d, at 704.</p>\n<p>Section 3205(a)(2) compels the disclosure, by a physician or a counselor, of information
        concerning the availability of paternal child support and state-funded alternatives if the woman decides to
        proceed with her pregnancy. Here again, the Court of Appeals observed that \"the record indicates that most
        clinics already require that a counselor consult in person with the woman about alternatives to abortion before
        the abortion is performed.\" <i>Id.,</i> at 704-705. And petitioners do not claim that the information required
        to be disclosed by statute is in any way false or inaccurate; indeed, the Court of Appeals found it to be
        \"relevant, accurate, and noninflammatory.\" <i>Id.,</i> at 705. We conclude that this required presentation of
        \"balanced information\" is rationally related to the State's legitimate interest in ensuring that the woman's
        consent is truly informed, <i>Thornburgh</i> v. <i>American College of Obstetricians and Gynecologists,</i> 476
        U. S., at 830 (O'Connor, J., dissenting), and in addition furthers the State's interest in preserving unborn
        life. That the information might create some uncertainty and persuade some women to forgo abortions does not
        lead to the conclusion that the Constitution forbids the provision of such information. Indeed, it only
        demonstrates that this information might <span class=\"star-pagination\">*969</span> very well make a
        difference, and that it is therefore relevant to a woman's informed choice. Cf. <i>id.,</i> at 801 (White, J.,
        dissenting) (\"[T]he ostensible objective of <i>Roe</i> v. <i>Wade</i> is not maximizing the number of
        abortions, but maximizing choice\"). We acknowledge that in <i>Thornburgh</i> this Court struck down informed
        consent requirements similar to the ones at issue here. See <i>id.,</i> at 760-764. It is clear, however, that
        while the detailed framework of <i>Roe</i> led to the Court's invalidation of those informational requirements,
        they \"would have been sustained under any traditional standard of judicial review, . . . or for any other
        surgical procedure except abortion.\" <i>Webster</i> v. <i>Reproductive Health Services,</i> 492 U. S., at 517
        (plurality opinion) (citing <i>Thornburgh</i> v. <i>American College of Obstetricians and Gynecologists,</i> 476
        U. S., at 802 (White, J., dissenting); <i>id.,</i> at 783 (Burger, C. J., dissenting)). In light of our
        rejection of <i>Roe</i> `s \"fundamental right\" approach to this subject, we do not regard <i>Thornburgh</i> as
        controlling.</p>\n<p>For the same reason, we do not feel bound to follow this Court's previous holding that a
        State's 24-hour mandatory waiting period is unconstitutional. See <i>Akron</i> v. <i>Akron Center for
            Reproductive Health, Inc., supra,</i> at 449-451. Petitioners are correct that such a provision will result
        in delays for some women that might not otherwise exist, therefore placing a burden on their liberty. But the
        provision in no way prohibits abortions, and the informed consent and waiting period requirements do not apply
        in the case of a medical emergency. See 18 Pa. Cons. Stat. §§ 3205(a), (b) (1990). We are of the view that, in
        providing time for reflection and reconsideration, the waiting period helps ensure that a woman's decision to
        abort is a well-considered one, and reasonably furthers the State's legitimate interest in maternal health and
        in the unborn life of the fetus. It \"is surely a small cost to impose to ensure that the woman's decision is
        well considered in light of its certain and irreparable consequences <span class=\"star-pagination\">*970</span>
        on fetal life, and the possible effects on her own.\" 462 U. S., at 474 (O'Connor, J., dissenting).</p>\n<p></p>
    \n<h2>B</h2>\n<p>In addition to providing her own informed consent, before an unemancipated woman under the age of
        18 may obtain an abortion she must either furnish the consent of one of her parents, or must opt for the
        judicial procedure that allows her to bypass the consent requirement. Under the judicial bypass option, a minor
        can obtain an abortion if a state court finds that she is capable of giving her informed consent and has indeed
        given such consent, <i>or</i> determines that an abortion is in her best interests. Records of these court
        proceedings are kept confidential. The Act directs the state trial court to render a decision within three days
        of the woman's application, and the entire procedure, including appeal to Pennsylvania Superior Court, is to
        last no longer than eight business days. The parental consent requirement does not apply in the case of a
        medical emergency. 18 Pa. Cons. Stat. § 3206 (1990). See Appendix to opinion of O'Connor, Kennedy, and Souter,
        JJ., <i>ante,</i> at 904-906.</p>\n<p>This provision is entirely consistent with this Court's previous decisions
        involving parental consent requirements. See <i>Planned Parenthood Assn. of Kansas City, Mo., Inc.</i> v.
        <i>Ashcroft,</i> 462 U. S. 476 (1983) (upholding parental consent requirement with a similar judicial bypass
        option); <i>Akron</i> v. <i>Akron Center for Reproductive Health, Inc., supra,</i> at 439-440 (approving of
        parental consent statutes that include a judicial bypass option allowing a pregnant minor to \"demonstrate that
        she is sufficiently mature to make the abortion decision herself or that, despite her immaturity, an abortion
        would be in her best interests\"); <i>Bellotti</i> v. <i>Baird,</i> 443 U. S. 622 (1979).
    </p>\n<p>We think it
        beyond dispute that a State \"has a strong and legitimate interest in the welfare of its young citizens, whose
        immaturity, inexperience, and lack of judgment may sometimes <span class=\"star-pagination\">*971</span> impair
        their ability to exercise their rights wisely.\" <i>Hodgson</i> v. <i>Minnesota,</i> 497 U. S., at 444 (opinion
        of Stevens, J.). A requirement of parental consent to abortion, like myriad other restrictions placed upon
        minors in other contexts, is reasonably designed to further this important and legitimate state interest. In our
        view, it is entirely \"rational and fair for the State to conclude that, in most instances, the family will
        strive to give a lonely or even terrified minor advice that is both compassionate and mature.\" <i>Ohio</i> v.
        <i>Akron Center for Reproductive Health,</i> 497 U. S., at 520 (opinion of Kennedy, J.); see also <i>Planned
            Parenthood of Central Mo.</i> v. <i>Danforth,</i> 428 U. S., at 91 (Stewart, J., concurring) (\"There can be
        little doubt that the State furthers a constitutionally permissible end by encouraging an unmarried pregnant
        minor to seek the help and advice of her parents in making the very important decision whether or not to bear a
        child\"). We thus conclude that Pennsylvania's parental consent requirement should be upheld.
    </p>\n<p></p>\n<h2>
        C</h2>\n<p>Section 3209 of the Act contains the spousal notification provision. It requires that, before a
        physician may perform an abortion on a married woman, the woman must sign a statement indicating that she has
        notified her husband of her planned abortion. A woman is not required to notify her husband if (1) her husband
        is not the father, (2) her husband, after diligent effort, cannot be located, (3) the pregnancy is the result of
        a spousal sexual assault that has been reported to the authorities, or (4) the woman has reason to believe that
        notifying her husband is likely to result in the infliction of bodily injury upon her by him or by another
        individual. In addition, a woman is exempted from the notification requirement in the case of a medical
        emergency. 18 Pa. Cons. Stat. § 3209 (1990). See Appendix to opinion of O'Connor, Kennedy, and Souter, JJ.,
        <i>ante,</i> at 908-909.
    </p>\n<p><span class=\"star-pagination\">*972</span> We first emphasize that
        Pennsylvania has not imposed a spousal <i>consent</i> requirement of the type the Court struck down in
        <i>Planned Parenthood of Central Mo.</i> v. <i>Danforth,</i> 428 U. S., at 67-72. Missouri's spousal consent
        provision was invalidated in that case because of the Court's view that it unconstitutionally granted to the
        husband \"a veto power exercisable for any reason whatsoever or for no reason at all.\" <i>Id.,</i> at 71. But
        the provision here involves a much less intrusive requirement of spousal <i>notification,</i> not consent. Such
        a law requiring only notice to the husband \"does not give any third party the legal right to make the [woman's]
        decision for her, or to prevent her from obtaining an abortion should she choose to have one performed.\"
        <i>Hodgson</i> v. <i>Minnesota, supra,</i> at 496 (Kennedy, J., concurring in judgment in part and dissenting in
        part); see <i>H. L.</i> v. <i>Matheson,</i> 450 U. S., at 411, n. 17. <i>Danforth</i> thus does not control our
        analysis. Petitioners contend that it should, however; they argue that the real effect of such a notice
        requirement is to give the power to husbands to veto a woman's abortion choice. The District Court indeed found
        that the notification provision created a risk that some woman who would otherwise have an abortion will be
        prevented from having one. 947 F. 2d, at 712. For example, petitioners argue, many notified husbands will
        prevent abortions through physical force, psychological coercion, and other types of threats. But Pennsylvania
        has incorporated exceptions in the notice provision in an attempt to deal with these problems. For instance, a
        woman need not notify her husband if the pregnancy is the result of a reported sexual assault, or if she has
        reason to believe that she would suffer bodily injury as a result of the notification. 18 Pa. Cons. Stat. §
        3209(b) (1990). Furthermore, because this is a facial challenge to the Act, it is insufficient for petitioners
        to show that the notification provision \"might operate unconstitutionally under some conceivable set of
        circumstances.\" <i>United States</i> v. <i>Salerno,</i> 481 U. S. 739, 745 (1987). Thus, it is not enough for
        petitioners <span class=\"star-pagination\">*973</span> to show that, in some \"worst case\" circumstances, the
        notice provision will operate as a grant of veto power to husbands. <i>Ohio</i> v. <i>Akron Center for
            Reproductive Health,</i> 497 U. S., at 514. Because they are making a facial challenge to the provision,
        they must \"show that no set of circumstances exists under which the [provision] would be valid.\" <i>Ibid.</i>
        (internal quotation marks omitted). This they have failed to do.<sup>[2]</sup>
    </p>\n<p><span class=\"star-pagination\">*974</span> The question before us is therefore whether the spousal
        notification
        requirement rationally furthers any legitimate state interests. We conclude that it does. First, a husband's
        interests in procreation within marriage and in the potential life of his unborn child are certainly substantial
        ones. See <i>Planned Parenthood of Central Mo.</i> v. <i>Danforth,</i> 428 U. S., at 69 (\"We are not unaware of
        the deep and proper concern and interest that a devoted and protective husband has in his wife's pregnancy and
        in the growth and development of the fetus she is carrying\"); <i>id.,</i> at 93 (White, J., concurring in part
        and dissenting in part); <i>Skinner</i> v. <i>Oklahoma ex rel. Williamson,</i> 316 U. S., at 541. The State
        itself has legitimate interests both in protecting these interests of the father and in protecting the potential
        life of the fetus, and the spousal notification requirement is reasonably related to advancing those state
        interests. By providing that a husband will usually know of his spouse's intent to have an abortion, the
        provision makes it more likely that the husband will participate in deciding the fate of his unborn child, a
        possibility that might otherwise have been denied him. This participation might in some cases result in a
        decision to proceed with the pregnancy. As Judge Alito observed in his dissent below, \"[t]he Pennsylvania
        legislature could have rationally believed that some married women are initially inclined to obtain an abortion
        without their husbands' knowledge because of perceived problemssuch as economic constraints, future plans, or
        the husbands' previously expressed <span class=\"star-pagination\">*975</span> oppositionthat may be obviated
        by discussion prior to the abortion.\" 947 F. 2d, at 726 (opinion concurring in part and dissenting in part).
    </p>\n<p>The State also has a legitimate interest in promoting \"the integrity of the marital relationship.\" 18 Pa.
        Cons. Stat. § 3209(a) (1990). This Court has previously recognized \"the importance of the marital relationship
        in our society.\" <i>Planned Parenthood of Central Mo.</i> v. <i>Danforth, supra,</i> at 69. In our view, the
        spousal notice requirement is a rational attempt by the State to improve truthful communication between spouses
        and encourage collaborative decision making, and thereby fosters marital integrity. See <i>Labine</i> v.
        <i>Vincent,</i> 401 U. S. 532, 538 (1971) (\"[T]he power to make rules to establish, protect, and strengthen
        family life\" is committed to the state legislatures). Petitioners argue that the notification requirement does
        not further any such interest; they assert that the majority of wives already notify their husbands of their
        abortion decisions, and the remainder have excellent reasons for keeping their decisions a secret. In the first
        case, they argue, the law is unnecessary, and in the second case it will only serve to foster marital discord
        and threats of harm. Thus, petitioners see the law as a totally irrational means of furthering whatever
        legitimate interest the State might have. But, in our view, it is unrealistic to assume that every husband-wife
        relationship is either (1) so perfect that this type of truthful and important communication will take place as
        a matter of course, or (2) so imperfect that, upon notice, the husband will react selfishly, violently, or
        contrary to the best interests of his wife. See <i>Planned Parenthood of Central Mo.</i> v. <i>Danforth,
            supra,</i> at 103-104 (Stevens, J., concurring in part and dissenting in part) (making a similar point in
        the context of a parental consent statute). The spousal notice provision will admittedly be unnecessary in some
        circumstances, and possibly harmful in others, but \"the existence of particular cases in which a feature of a
        statute performs no function (or is even counter productive) <span class=\"star-pagination\">*976</span>
        ordinarily does not render the statute unconstitutional or even constitutionally suspect.\" <i>Thornburgh</i> v.
        <i>American College of Obstetricians and Gynecologists,</i> 476 U. S., at 800 (White, J., dissenting). The
        Pennsylvania Legislature was in a position to weigh the likely benefits of the provision against its likely
        adverse effects, and presumably concluded, on balance, that the provision would be beneficial. Whether this was
        a wise decision or not, we cannot say that it was irrational. We therefore conclude that the spousal notice
        provision comports with the Constitution. See <i>Harris</i> v. <i>McRae,</i> 448 U. S., at 325-326 (\"It is not
        the mission of this Court or any other to decide whether the balance of competing interests . . . is wise social
        policy\").
    </p>\n<p></p>\n<h2>D</h2>\n<p>The Act also imposes various reporting requirements. Section 3214(a)
        requires that abortion facilities file a report on each abortion performed. The reports do not include the
        identity of the women on whom abortions are performed, but they do contain a variety of information about the
        abortions. For example, each report must include the identities of the performing and referring physicians, the
        gestational age of the fetus at the time of abortion, and the basis for any medical judgment that a medical
        emergency existed. See 18 Pa. Cons. Stat. §§ 3214(a)(1), (5), (10) (1990). See Appendix to opinion of O'Connor,
        Kennedy, and Souter, JJ., <i>ante,</i> at 909-911. The District Court found that these reports are kept
        completely confidential. 947 F. 2d, at 716. We further conclude that these reporting requirements rationally
        further the State's legitimate interests in advancing the state of medical knowledge concerning maternal health
        and prenatal life, in gathering statistical information with respect to patients, and in ensuring compliance
        with other provisions of the Act.</p>\n<p>Section 3207 of the Act requires each abortion facility to file a
        report with its name and address, as well as the names <span class=\"star-pagination\">*977</span> and addresses
        of any parent, subsidiary, or affiliated organizations. 18 Pa. Cons. Stat. § 3207(b) (1990). Section 3214(f)
        further requires each facility to file quarterly reports stating the total number of abortions performed, broken
        down by trimester. Both of these reports are available to the public only if the facility received state funds
        within the preceding 12 months. See Appendix to opinion of O'Connor, Kennedy, and Souter, JJ., <i>ante,</i> at
        906, 911. Petitioners do not challenge the requirement that facilities provide this information. They contend,
        however, that the forced public disclosure of the information given by facilities receiving public funds serves
        no legitimate state interest. We disagree. Records relating to the expenditure of public funds are generally
        available to the public under Pennsylvania law. See Pa. Stat. Ann., Tit. 65, §§ 66.1, 66.2 (Purdon 1959 and
        Supp. 1991-1992). As the Court of Appeals observed, \"[w]hen a state provides money to a private commercial
        enterprise, there is a legitimate public interest in informing taxpayers who the funds are benefiting and what
        services the funds are supporting.\" 947 F. 2d, at 718. These reporting requirements rationally further this
        legitimate state interest.</p>\n<p></p>\n<h2>E</h2>\n<p>Finally, petitioners challenge the medical emergency
        exception provided for by the Act. The existence of a medical emergency exempts compliance with the Act's
        informed consent, parental consent, and spousal notice requirements. See 18 Pa. Cons. Stat. §§ 3205(a), 3206(a),
        3209(c) (1990). The Act defines a \"medical emergency\" as</p>\n<blockquote>\"[t]hat condition which, on the
        basis of the physician's good faith clinical judgment, so complicates the medical condition of a pregnant woman
        as to necessitate the immediate abortion of her pregnancy to avert her death or for which a delay will create
        serious risk of substantial <span class=\"star-pagination\">*978</span> and irreversible impairment of major
        bodily function.\" § 3203.</blockquote>\n<p>Petitioners argued before the District Court that the statutory
        definition was inadequate because it did not cover three serious conditions that pregnant women can suffer
        preeclampsia, inevitable abortion, and prematurely ruptured membrane. The District Court agreed with petitioners
        that the medical emergency exception was inadequate, but the Court of Appeals reversed this holding. In
        construing the medical emergency provision, the Court of Appeals first observed that all three conditions do
        indeed present the risk of serious injury or death when an abortion is not performed, and noted that the medical
        profession's uniformly prescribed treatment for each of the three conditions is an immediate abortion. See 947
        F. 2d, at 700-701. Finding that \"[t]he Pennsylvania legislature did not choose the wording of its medical
        emergency exception in a vacuum,\" the court read the exception as intended \"to assure that compliance with its
        abortion regulations would not in any way pose a significant threat to the life or health of a woman.\"
        <i>Id.,</i> at 701. It thus concluded that the exception encompassed each of the three dangerous conditions
        pointed to by petitioners.
    </p>\n<p>We observe that Pennsylvania's present definition of medical emergency is
        almost an exact copy of that State's definition at the time of this Court's ruling in <i>Thornburgh,</i> one
        which the Court made reference to with apparent approval. 476 U. S., at 771 (\"It is clear that the Pennsylvania
        Legislature knows how to provide a medical-emergency exception when it chooses to do so\").<sup>[3]</sup> We
        find that the interpretation <span class=\"star-pagination\">*979</span> of the Court of Appeals in these cases
        is eminently reasonable, and that the provision thus should be upheld. When a woman is faced with any condition
        that poses a \"significant threat to [her] life or health,\" she is exempted from the Act's consent and notice
        requirements and may proceed immediately with her abortion.</p>\n<p></p>\n<h2>IV</h2>\n<p>For the reasons
        stated, we therefore would hold that each of the challenged provisions of the Pennsylvania statute is consistent
        with the Constitution. It bears emphasis that our conclusion in this regard does not carry with it any necessary
        approval of these regulations. Our task is, as always, to decide only whether the challenged provisions of a law
        comport with the United States Constitution. If,as we believe,these do,their wisdom as a matter of public policy
        is for the people of Pennsylvania to decide.</p>\n<p>Justice Scalia, with whom The Chief Justice, Justice White,
        and Justice Thomas join, concurring in the judgment in part and dissenting in part.</p>\n<p>My views on this
        matter are unchanged from those I set forth in my separate opinions in <i>Webster</i> v. <i>Reproductive Health
            Services,</i> 492 U. S. 490, 532 (1989) (opinion concurring in part and concurring in judgment), and
        <i>Ohio</i> v. <i>Akron Center for Reproductive Health,</i> 497 U. S. 502, 520 (1990) <i>(Akron II)</i>
        (concurring opinion). The States may, if they wish, permit abortion on demand, but the Constitution does not
        <i>require</i> them to do so. The permissibility of abortion, and the limitations upon it, are to be resolved
        like most important questions in our democracy: by citizens trying to persuade one another and then voting. As
        the Court acknowledges, \"where reasonable people disagree the government can adopt one position or the other.\"
        <i>Ante,</i> at 851. The Court is correct in adding the qualification that this \"assumes a state of affairs in
        which the choice does not intrude upon a protected liberty,\" <i>ibid.</i> but the crucial part of that
        qualification <span class=\"star-pagination\">*980</span> is the penultimate word. A State's choice between two
        positions on which reasonable people can disagree is constitutional even when (as is often the case) it intrudes
        upon a \"liberty\" in the absolute sense. Laws against bigamy, for examplewith which entire societies of
        reasonable people disagreeintrude upon men and women's liberty to marry and live with one another. But bigamy
        happens not to be a liberty specially \"protected\" by the Constitution.
    </p>\n<p>That is, quite simply, the
        issue in these cases: not whether the power of a woman to abort her unborn child is a \"liberty\" in the
        absolute sense; or even whether it is a liberty of great importance to many women. Of course it is both. The
        issue is whether it is a liberty protected by the Constitution of the United States. I am sure it is not. I
        reach that conclusion not because of anything so exalted as my views concerning the \"concept of existence, of
        meaning, of the universe, and of the mystery of human life.\" <i>Ibid.</i> Rather, I reach it for the same
        reason I reach the conclusion that bigamy is not constitutionally protectedbecause of two simple facts: (1) the
        Constitution says absolutely nothing about it, and (2) the longstanding traditions of American society have
        permitted it to be legally proscribed.<sup>[1]</sup><i>Akron II, supra,</i> at 520 (Scalia, J., concurring).</p>
    \n<p><span class=\"star-pagination\">*981</span> The Court destroys the proposition, evidently meant to represent my
        position, that \"liberty\" includes \"only those practices, defined at the most specific level, that were
        protected against government interference by other rules of law when the Fourteenth Amendment was ratified,\"
        <i>ante,</i> at 847 (citing <i>Michael H.</i> v. <i>Gerald D.,</i> 491 U. S. 110, 127, n. 6 (1989) (opinion of
        Scalia, J.)). That is not, however, what <i>Michael H.</i> says; it merely observes that, in defining
        \"liberty,\" we may not disregard a specific, \"relevant tradition protecting, or denying protection to, the
        asserted right,\" <i>ibid.</i> But the Court does not wish to be fettered by any such limitations on its
        preferences. The Court's statement that it is \"tempting\" to acknowledge the authoritativeness of tradition in
        order to \"cur[b] the discretion of federal judges,\" <i>ante,</i> at 847, is of course rhetoric rather than
        reality; no government official is \"tempted\" to place restraints upon his own freedom of action, which is why
        Lord Act on did not say \"Power tends to purify.\" The Court's temptation is in the quite opposite and more
        natural directiontowards systematically eliminating checks upon its own power; and it succumbs.
    </p>\n<p>Beyond
        that brief summary of the essence of my position, I will not swell the United States Reports with repetition of
        what I have said before; and applying the rational basis test, I would uphold the Pennsylvania statute in its
        entirety. I must, however, respond to a few of the more outrageous arguments in today's opinion, which it is
        beyond human nature to leave unanswered. I shall discuss each of them under a quotation from the Court's opinion
        to which they pertain.</p>\n<blockquote>\"The inescapable fact is that adjudication of sub- stantive due process
        claims may call upon the Court</blockquote>\n<blockquote>\n<span class=\"star-pagination\">*982</span> in
        interpreting the Constitution to exercise that same capacity which by tradition courts always have exercised:
        reasoned judgment.\" <i>Ante,</i> at 849.</blockquote>\n<p>Assuming that the question before us is to be
        resolved at such a level of philosophical abstraction, in such isolation from the traditions of American
        society, as by simply applying \"reasoned judgment,\" I do not see how that could possibly have produced the
        answer the Court arrived at in <i>Roe</i> v. <i>Wade,</i> 410 U. S. 113 (1973). Today's opinion describes the
        methodology of <i>Roe,</i> quite accurately, as weighing against the woman's interest the State's \"`important
        and legitimate interest in protecting the potentiality of human life.' \" <i>Ante,</i> at 871 (quoting <i>Roe,
            supra,</i> at 162). But \"reasoned judgment\" does not begin by begging the question, as <i>Roe</i> and
        subsequent cases unquestionably did by assuming that what the State is protecting is the mere \"potentiality of
        human life.\" See, <i>e. g., </i><i>Roe, supra,</i> at 162; <i>Planned Parenthood of Central Mo.</i> v.
        <i>Danforth,</i> 428 U. S. 52, 61 (1976); <i>Colautti</i> v. <i>Franklin,</i> 439 U. S. 379, 386 (1979);
        <i>Akron</i> v. <i>Akron Center for Reproductive Health, Inc.,</i> 462 U. S. 416, 428 (1983) <i>(Akron
            I)</i><i>; </i><i>Planned Parenthood Assn. of Kansas City, Mo., Inc.</i> v. <i>Ashcroft,</i> 462 U. S. 476,
        482 (1983). The whole argument of abortion opponents is that what the Court calls the fetus and what others call
        the unborn child <i>is a human life.</i> Thus, whatever answer <i>Roe</i> came up with after conducting its
        \"balancing\" is bound to be wrong, unless it is correct that the human fetus is in some critical sense merely
        potentially human. There is of course no way to determine that as a legal matter; it is in fact a value
        judgment. Some societies have considered newborn children not yet human, or the incompetent elderly no longer
        so.
    </p>\n<p>The authors of the joint opinion, of course, do not squarely contend that <i>Roe</i> v. <i>Wade</i>
        was a <i>correct</i> application of \"reasoned judgment\"; merely that it must be followed, because of <i>stare
            decisis. Ante,</i> at 853, 861, 871. But in their exhaustive discussion of all the factors that go into the
        determination <span class=\"star-pagination\">*983</span> of when <i>stare decisis</i> should be observed and
        when disregarded, they never mention \"how wrong was the decision on its face?\" Surely, if \"[t]he Court's
        power lies . .. in its legitimacy, a product of substance and perception,\" <i>ante,</i> at 865, the
        \"substance\" part of the equation demands that plain error be acknowledged and eliminated. <i>Roe</i> was
        plainly wrongeven on the Court's methodology of \"reasoned judgment,\" and even more so (of course) if the
        proper criteria of text and tradition are applied.</p>\n<p>The emptiness of the \"reasoned judgment\" that
        produced <i>Roe</i> is displayed in plain view by the fact that, after more than 19 years of effort by some of
        the brightest (and most determined) legal minds in the country, after more than 10 cases upholding abortion
        rights in this Court, and after dozens upon dozens of <i>amicus</i> briefs submitted in these and other cases,
        the best the Court can do to explain how it is that the word \"liberty\" <i>must</i> be thought to include the
        right to destroy human fetuses is to rattle off a collection of adjectives that simply decorate a value judgment
        and conceal a political choice. The right to abort, we are told, inheres in \"liberty\" because it is among \"a
        person's most basic decisions,\" <i>ante,</i> at 849; it involves a \"most intimate and personal choic[e],\"
        <i>ante,</i> at 851; it is \"central to personal dignity and autonomy,\" <i>ibid.;</i> it \"originate[s] within
        the zone of conscience and belief,\" <i>ante,</i> at 852; it is \"too intimate and personal\" for state
        interference, <i>ibid.;</i> it reflects \"intimate views\" of a \"deep, personal character,\" <i>ante,</i> at
        853; it involves \"intimate relationships\" and notions of \"personal autonomy and bodily integrity,\"
        <i>ante,</i> at 857; and it concerns a particularly \"`important decisio[n],' \" <i>ante,</i> at 859 (citation
        omitted).<sup>[2]</sup> But it is <span class=\"star-pagination\">*984</span> obvious to anyone applying
        \"reasoned judgment\" that the same adjectives can be applied to many forms of conduct that this Court
        (including one of the Justices in today's majority, see <i>Bowers</i> v. <i>Hardwick,</i> 478 U. S. 186 (1986))
        has held are <i>not</i> entitled to constitutional protectionbecause, like abortion, they are forms of conduct
        that have long been criminalized in American society. Those adjectives might be applied, for example, to
        homosexual sodomy, polygamy, adult incest, and suicide, all of which are equally \"intimate\" and \"deep[ly]
        personal\" decisions involving \"personal autonomy and bodily integrity,\" and all of which can constitutionally
        be proscribed because it is our unquestionable constitutional tradition that they are proscribable. It is not
        reasoned judgment that supports the Court's decision; only personal predilection. Justice Curtis's warning is as
        timely today as it was 135 years ago:
    </p>\n<blockquote>\"[W]hen a strict interpretation of the Constitution,
        according to the fixed rules which govern the interpretation of laws, is abandoned, and the theoretical opinions
        of individuals are allowed to control its meaning, we have no longer a Constitution; we are under the government
        of individual men, who for the time being have power to declare what the Constitution is, according to their own
        views of what it ought to mean.\" <i>Dred Scott</i> v. <i>Sandford,</i> 19 How. 393, 621 (1857) (dissenting
        opinion). \"Liberty finds no refuge in a jurisprudence of doubt.\" <i>Ante,</i> at 844.</blockquote>\n<p>One
        might have feared to encounter this august and sonorous phrase in an opinion defending the real <i>Roe</i> v.
        <i>Wade</i><i>,</i> rather than the revised version fabricated today by the authors <span
            class=\"star-pagination\">*985</span> of the joint opinion. The shortcomings of <i>Roe</i> did not include
        lack of clarity: Virtually all regulation of abortion before the third trimester was invalid. But to come across
        this phrase in the joint opinionwhich calls upon federal district judges to apply an \"undue burden\" standard
        as doubtful in application as it is unprincipled in originis really more than one should have to bear.
    </p>\n<p>
        The joint opinion frankly concedes that the amorphous concept of \"undue burden\" has been inconsistently
        applied by the Members of this Court in the few brief years since that \"test\" was first explicitly propounded
        by Justice O'Connor in her dissent in <i>Akron I,</i> 462 U. S. 416 (1983). See <i>ante,</i> at
        876.<sup>[3]</sup> Because the three Justices now wish to \"set forth a standard of general application,\" the
        joint opinion announces that \"it is important to clarify what is meant by an undue burden.\" <i>Ibid.</i> I
        certainly agree with that, but I do not agree that the joint opinion succeeds in the announced endeavor. To the
        contrary, its efforts at clarification <span class=\"star-pagination\">*986</span> make clear only that the
        standard is inherently manipulable and will prove hopelessly unworkable in practice.</p>\n<p>The joint opinion
        explains that a state regulation imposes an \"undue burden\" if it \"has the purpose or effect of placing a
        substantial obstacle in the path of a woman seeking an abortion of a nonviable fetus.\" <i>Ante,</i> at 877; see
        also <i>ante,</i> at 877-879. An obstacle is \"substantial,\" we are told, if it is \"calculated[,] [not] to
        inform the woman's free choice, [but to] hinder it.\" <i>Ante,</i> at 877.<sup>[4]</sup> This latter statement
        cannot <span class=\"star-pagination\">*987</span> possibly mean what it says. <i>Any</i> regulation of abortion
        that is intended to advance what the joint opinion concedes is the State's \"substantial\" interest in
        protecting unborn life will be \"calculated [to] hinder\" a decision to have an abortion. It thus seems more
        accurate to say that the joint opinion would uphold abortion regulations only if they do not <i>unduly</i>
        hinder the woman's decision. That, of course, brings us right back to square one: Defining an \"undue burden\"
        as an \"undue hindrance\" (or a \"substantial obstacle\") hardly \"clarifies\" the test. Consciously or not, the
        joint opinion's verbal shell game will conceal raw judicial policy choices concerning what is \"appropriate\"
        abortion legislation.</p>\n<p>The ultimately standard less nature of the \"undue burden\" inquiry is a
        reflection of the underlying fact that the concept has no principled or coherent legal basis. As The Chief
        Justice points out, <i>Roe</i> `s strict-scrutiny standard \"at least had a recognized basis in constitutional
        law at the time <i>Roe</i> was decided,\" <i>ante,</i> at 964, while \"[t]he same cannot be said for the `undue
        burden' standard, which is created largely out of whole cloth by the authors of the joint opinion,\"
        <i>ibid.</i> The joint opinion is flatly wrong in asserting that \"our jurisprudence relating to all liberties
        save perhaps abortion has recognized\" the permissibility of laws that do not impose an \"undue burden.\"
        <i>Ante,</i> at 873. It argues that the abortion right is similar to other rights in that a law \"not designed
        to strike at the right itself, [but which] has the incidental effect of making it more difficult or more
        expensive to [exercise the right,]\" is not invalid. <i>Ante,</i> at 874. I agree, indeed I have <span
            class=\"star-pagination\">*988</span> forcefully urged, that a law of general applicability which places
        only an incidental burden on a fundamental right does not infringe that right, see <i>R. A. V.</i> v. <i>St.
            Paul,</i> 505 U. S. 377, 389-390 (1992); <i>Employment Div., Dept. of Human Resources of Ore.</i> v.
        <i>Smith,</i> 494 U. S. 872, 878-882 (1990), but that principle does not establish the quite different (and
        quite dangerous) proposition that a law which <i>directly</i> regulates a fundamental right will not be found to
        violate the Constitution unless it imposes an \"undue burden.\" It is that, of course, which is at issue here:
        Pennsylvania has <i>consciously and directly</i> regulated conduct that our cases have held is constitutionally
        protected. The appropriate analogy, therefore, is that of a state law requiring purchasers of religious books to
        endure a 24-hour waiting period, or to pay a nominal additional tax of 1¢. The joint opinion cannot possibly be
        correct in suggesting that we would uphold such legislation on the ground that it does not impose a
        \"substantial obstacle\" to the exercise of First Amendment rights. The \"undue burden\" standard is not at all
        the generally applicable principle the joint opinion pretends it to be; rather, it is a unique concept created
        specially for these cases, to preserve some judicial foothold in this ill-gotten territory. In claiming
        otherwise, the three Justices show their willingness to place all constitutional rights at risk in an effort to
        preserve what they deem the \"central holding in <i>Roe.</i> \" <i>Ante,</i> at 873.
    </p>\n<p>The rootless nature
        of the \"undue burden\" standard, a phrase plucked out of context from our earlier abortion decisions, see n. 3,
        <i>supra,</i> is further reflected in the fact that the joint opinion finds it necessary expressly to repudiate
        the more narrow formulations used in Justice O'Connor's earlier opinions. <i>Ante,</i> at 876-877. Those
        opinions stated that a statute imposes an \"undue burden\" if it imposes \"<i>absolute</i> obstacles or
        <i>severe</i> limitations on the abortion decision,\" <i>Akron I,</i> 462 U. S., at 464 (dissenting opinion)
        (emphasis added); see also <i>Thornburgh</i> v. <i>American College of Obstetricians and Gynecologists,</i> 476
        U. S. 747, 828 (1986) (dissenting <span class=\"star-pagination\">*989</span> opinion). Those strong adjectives
        are conspicuously missing from the joint opinion, whose authors have for some unexplained reason now determined
        that a burden is \"undue\" if it merely imposes a \"substantial\" obstacle to abortion decisions. See, <i>e. g.,
            ante,</i> at 895, 901. Justice O'Connor has also abandoned (again without explanation) the view she
        expressed in <i>Planned Parenthood Assn. of Kansas City, Mo., Inc.</i> v. <i>Ashcroft,</i> 462 U. S. 476 (1983)
        (dissenting opinion), that a medical regulation which imposes an \"undue burden\" could nevertheless be upheld
        if it \"reasonably relate[s] to the preservation and protection of maternal health,\" <i>id.,</i> at 505
        (citation and internal quotation marks omitted). In today's version, even health measures will be upheld only
        \"<i>if they do not constitute an undue burden,</i>\" <i>ante,</i> at 878 (emphasis added). Gone too is Justice
        O'Connor's statement that \"the State possesses <i>compelling</i> interests in the protection of potential human
        life . . . throughout pregnancy,\" <i>Akron I, supra,</i> at 461 (dissenting opinion) (emphasis added); see also
        <i>Ashcroft, supra,</i> at 505 (O'Connor, J., concurring in judgment in part and dissenting in part);
        <i>Thornburgh, supra,</i> at 828 (O'Connor, J., dissenting); instead, the State's interest in unborn human life
        is stealthily downgraded to a merely \"substantial\" or \"profound\" interest, <i>ante,</i> at 876, 878. (That
        had to be done, of course, since designating the interest as \"compelling\" throughout pregnancy would have
        been, shall we say, a \"substantial obstacle\" to the joint opinion's determined effort to reaffirm what it
        views as the \"central holding\" of <i>Roe.</i> See <i>Akron I,</i> 462 U. S., at 420, n. 1.) And \"viability\"
        is no longer the \"arbitrary\" dividing line previously decried by Justice O'Connor in <i>Akron I, id.,</i> at
        461; the Court now announces that \"the attainment of viability may continue to serve as the critical fact,\"
        <i>ante,</i> at 860.<sup>[5]</sup> It is difficult to <span class=\"star-pagination\">*990</span> maintain the
        illusion that we are interpreting a Constitution rather than inventing one, when we amend its provisions so
        breezily.
    </p>\n<p>Because the portion of the joint opinion adopting and describing the undue burden test
        provides no more useful guidance than the empty phrases discussed above, one must turn to the 23 pages applying
        that standard to the present facts for further guidance. In evaluating Pennsylvania's abortion law, the joint
        opinion relies extensively on the factual findings of the District Court, and repeatedly qualifies its
        conclusions by noting that they are contingent upon the record developed in these cases. Thus, the joint opinion
        would uphold the 24-hour waiting period contained in the Pennsylvania statute's informed consent provision, 18
        Pa. Cons. Stat. § 3205 (1990), because \"the record evidence shows that in the vast majority of cases, a 24-hour
        delay does not create any appreciable health risk,\" <i>ante,</i> at 885. The three Justices therefore conclude
        that \"on the record before us, . . . we are not convinced that the 24-hour waiting period constitutes an undue
        burden.\" <i>Ante,</i> at 887. The requirement that a doctor provide the information pertinent to informed
        consent would also be upheld because \"there is no evidence on this record that [this requirement] would amount
        in practical terms to a substantial obstacle to a woman seeking an abortion.\" <i>Ante,</i> at 884. Similarly,
        the joint opinion would uphold the reporting requirements of the Act, §§ 3207, 3214, because \"there is no . . .
        showing on the record before us\" that these requirements constitute a \"substantial obstacle\" <span
            class=\"star-pagination\">*991</span> to abortion decisions. <i>Ante,</i> at 901. But at the same time the
        opinion pointedly observes that these reporting requirements may increase the costs of abortions and that \"at
        some point [that fact] could become a substantial obstacle.\" <i>Ibid.</i> Most significantly, the joint
        opinion's conclusion that the spousal notice requirement of the Act, see § 3209, imposes an \"undue burden\" is
        based in large measure on the District Court's \"detailed findings of fact,\" which the joint opinion sets out
        at great length, <i>ante,</i> at 888-891.</p>\n<p>I do not, of course, have any objection to the notion that, in
        applying legal principles, one should rely only upon the facts that are contained in the record or that are
        properly subject to judicial notice.<sup>[6]</sup> But what is remarkable about the joint opinion's
        fact-intensive analysis is that it does not result in any measurable clarification of the \"undue burden\"
        standard. Rather, the approach of the joint opinion is, for the most part, simply to highlight certain facts in
        the record that apparently strike the three Justices as particularly significant in establishing (or refuting)
        the existence of an undue burden; after describing these facts, the opinion then simply announces that the
        provision either does or does not impose a \"substantial obstacle\" or an \"undue burden.\" See, <i>e. g.,
            ante,</i> at 880, 884-885, 887, 893-894, 895, 901. We do not know whether the same conclusions could have
        been reached on a different record, or in what respects the record would have had to differ before an opposite
        conclusion would have been <span class=\"star-pagination\">*992</span> appropriate. The inherently standard less
        nature of this inquiry invites the district judge to give effect to his personal preferences about abortion. By
        finding and relying upon the right facts, he can invalidate, it would seem, almost any abortion restriction that
        strikes him as \"undue\"subject, of course, to the possibility of being reversed by a court of appeals or
        Supreme Court that is as unconstrained in reviewing his decision as he was in making it.</p>\n<p>To the extent I
        can discern <i>any</i> meaningful content in the \"undue burden\" standard as applied in the joint opinion, it
        appears to be that a State may not regulate abortion in such a way as to reduce significantly its incidence. The
        joint opinion repeatedly emphasizes that an important factor in the \"undue burden\" analysis is whether the
        regulation \"prevent[s] a significant number of women from obtaining an abortion,\" <i>ante,</i> at 893; whether
        a \"significant number of women . . . are likely to be deterred from procuring an abortion,\" <i>ante,</i> at
        894; and whether the regulation often \"deters\" women from seeking abortions, <i>ante,</i> at 897. We are not
        told, however, what forms of \"deterrence\" are impermissible or what degree of success in deterrence is too
        much to be tolerated. If, for example, a State required a woman to read a pamphlet describing, with
        illustrations, the facts of fetal development before she could obtain an abortion, the effect of such
        legislation might be to \"deter\" a \"significant number of women\" from procuring abortions, thereby seemingly
        allowing a district judge to invalidate it as an undue burden. Thus, despite flowery rhetoric about the State's
        \"substantial\" and \"profound\" interest in \"potential human life,\" and criticism of <i>Roe</i> for
        undervaluing that interest, the joint opinion permits the State to pursue that interest only so long as it is
        not too successful. As Justice Blackmun recognizes (with evident hope), <i>ante,</i> at 926, the \"undue
        burden\" standard may ultimately require the invalidation of each provision upheld today if it can be shown, on
        a better record, that the State is too effectively \"express[ing] a preference <span
            class=\"star-pagination\">*993</span> for childbirth over abortion,\" <i>ante,</i> at 883. Reason finds no
        refuge in this jurisprudence of confusion.</p>\n<blockquote>\"While we appreciate the weight of the arguments .
        . that <i>Roe</i> should be overruled, the reservations any of us may have in reaffirming the central holding of
        <i>Roe</i> are outweighed by the explication of individ- ual liberty we have given combined with the force of
        <i>stare decisis.</i>\" <i>Ante,</i> at 853.
    </blockquote>\n<p>The Court's reliance upon <i>stare decisis</i> can
        best be described as contrived. It insists upon the necessity of adhering not to all of <i>Roe,</i> but only to
        what it calls the \"central holding.\" It seems to me that <i>stare decisis</i> ought to be applied even to the
        doctrine of <i>stare decisis,</i> and I confess never to have heard of this new,
        keep-what-you-want-and-throwaway-the-rest version. I wonder whether, as applied to <i>Marbury</i> v.
        <i>Madison,</i> 1 Cranch 137 (1803), for example, the new version of <i>stare decisis</i> would be satisfied if
        we allowed courts to review the constitutionality of only those statutes that (like the one in <i>Marbury</i>)
        pertain to the jurisdiction of the courts.
    </p>\n<p>I am certainly not in a good position to dispute that the
        Court <i>has saved</i> the \"central holding\" of <i>Roe,</i> since to do that effectively I would have to know
        what the Court has saved, which in turn would require me to understand (as I do not) what the \"undue burden\"
        test means. I must confess, however, that I have always thought, and I think a lot of other people have always
        thought, that the arbitrary trimester framework, which the Court today discards, was quite as central to
        <i>Roe</i> as the arbitrary viability test, which the Court today retains. It seems particularly ungrateful to
        carve the trimester framework out of the core of <i>Roe,</i> since its very rigidity (in sharp contrast to the
        utter indeterminability of the \"undue burden\" test) is probably the only reason the Court is able to say, in
        urging <i>stare decisis,</i> that <i>Roe</i> \"has in no sense proven `unworkable,' \" <i>ante,</i> at 855. I
        suppose the <span class=\"star-pagination\">*994</span> Court is entitled to call a \"central holding\" whatever
        it wants to call a \"central holding\"which is, come to think of it, perhaps one of the difficulties with this
        modified version of <i>stare decisis.</i> I thought I might note, however, that the following portions of
        <i>Roe</i> have not been saved:
    </p>\n<p> Under <i>Roe,</i> requiring that a woman seeking an abortion be
        provided truthful information about abortion before giving informed written consent is unconstitutional, if the
        information is designed to influence her choice. <i>Thornburgh,</i> 476 U. S., at 759-765; <i>Akron I,</i> 462
        U. S., at 442-445. Under the joint opinion's \"undue burden\" regime (as applied today, at least) such a
        requirement is constitutional. <i>Ante,</i> at 881-885.</p>\n<p> Under <i>Roe,</i> requiring that information
        be provided by a doctor, rather than by nonphysician counselors, is unconstitutional. <i>Akron I, supra,</i> at
        446-449. Under the \"undue burden\" regime (as applied today, at least) it is not. <i>Ante,</i> at 884-885.</p>
    \n<p> Under <i>Roe,</i> requiring a 24-hour waiting period between the time the woman gives her informed consent
        and the time of the abortion is unconstitutional. <i>Akron I, supra,</i> at 449-451. Under the \"undue burden\"
        regime (as applied today, at least) it is not. <i>Ante,</i> at 885-887.</p>\n<p> Under <i>Roe,</i> requiring
        detailed reports that include demographic data about each woman who seeks an abortion and various information
        about each abortion is unconstitutional. <i>Thornburgh, supra,</i> at 765-768. Under the \"undue burden\" regime
        (as applied today, at least) it generally is not. <i>Ante,</i> at 900-901.</p>\n<blockquote>\"Where, in the
        performance of its judicial duties, the Court decides a case in such a way as to resolve the sort of intensely
        divisive controversy reflected in <i>Roe</i> . . . , its decision has a dimension that the resolu- tion of the
        normal case does not carry. It is the di- mension present whenever the Court's interpretation of the
        Constitution calls the contending sides of a</blockquote>\n<blockquote>\n<span
            class=\"star-pagination\">*995</span> national controversy to end their national division by accepting a
        common mandate rooted in the Con- stitution.\" <i>Ante,</i> at 866-867.</blockquote>\n<p>The Court's description
        of the place of <i>Roe</i> in the social history of the United States is unrecognizable. Not only did <i>Roe</i>
        not, as the Court suggests, <i>resolve</i> the deeply divisive issue of abortion; it did more than anything else
        to nourish it, by elevating it to the national level where it is infinitely more difficult to resolve. National
        politics were not plagued by abortion protests, national abortion lobbying, or abortion marches on Congress
        before <i>Roe</i> v. <i>Wade</i> was decided. Profound disagreement existed among our citizens over the issueas
        it does over other issues, such as the death penaltybut that disagreement was being worked out at the state
        level. As with many other issues, the division of sentiment within each State was not as closely balanced as it
        was among the population of the Nation as a whole, meaning not only that more people would be satisfied with the
        results of state-by-state resolution, but also that those results would be more stable. Pre-<i>Roe,</i>
        moreover, political compromise was possible.</p>\n<p><i>Roe</i> `s mandate for abortion on demand destroyed the
        compromises of the past, rendered compromise impossible for the future, and required the entire issue to be
        resolved uniformly, at the national level. At the same time, <i>Roe</i> created a vast new class of abortion
        consumers and abortion proponents by eliminating the moral opprobrium that had attached to the act. (\"If the
        Constitution <i>guarantees</i> abortion, how can it be bad?\"not an accurate line of thought, but a natural
        one.) Many favor all of those developments, and it is not for me to say that they are wrong. But to portray
        <i>Roe</i> as the states manlike \"settlement\" of a divisive issue, a jurisprudential Peace of Westphalia that
        is worth preserving, is nothing less than Orwellian. <i>Roe</i> fanned into life an issue that has inflamed our
        national politics in general, and has obscured with its smoke the selection of Justices to this Court <span
            class=\"star-pagination\">*996</span> in particular, ever since. And by keeping us in the abortionumpiring
        business, it is the perpetuation of that disruption, rather than of any <i>Pax Roeana,</i> that the Court's new
        majority decrees.
    </p>\n<blockquote>\"[T]o overrule under fire . . . would subvert the Court's legitimacy . . . .
        \". . . To all those who will be . . . tested by follow- ing, the Court implicitly undertakes to remain stead-
        fast . . . . The promise of constancy, once given, binds its maker for as long as the power to stand by the
        decision survives and . . . the commitment [is not] obsolete. . . .</blockquote>\n<blockquote>\"[The American
        people's] belief in themselves as . . . a people [who aspire to live according to the rule of law] is not
        readily separable from their under- standing of the Court invested with the authority to decide their
        constitutional cases and speak before all others for their constitutional ideals. If the Court's legitimacy
        should be undermined, then, so would the country be in its very ability to see itself through its constitutional
        ideals.\" <i>Ante,</i> at 867-868.</blockquote>\n<p>The Imperial Judiciary lives. It is instructive to compare
        this Nietzschean vision of us unelected, life-tenured judges leading a Volk who will be \"tested by
        following,\" and whose very \"belief in themselves\" is mystically bound up in their \"understanding\" of a
        Court that \"speak[s] before all others for their constitutional ideals\"with the somewhat more modest role
        envisioned for these lawyers by the Founders.</p>\n<blockquote>\"The judiciary . . . has . . . no direction
        either of the strength or of the wealth of the society, and can take no active resolution whatever. It may truly
        be said to have neither Force nor Will, but merely judgment . . . .\"</blockquote>\n<p>The Federalist No. 78,
        pp. 393-394 (G. Wills ed. 1982). Or, again, to compare this ecstasy of a Supreme Court in which there is,
        especially on controversial matters, no <span class=\"star-pagination\">*997</span> shadow of change or hint of
        alteration (\"There is a limit to the amount of error that can plausibly be imputed to prior Courts,\"
        <i>ante,</i> at 866), with the more democratic views of a more humble man:
    </p>\n<blockquote>\"[T]he candid
        citizen must confess that if the policy of the Government upon vital questions affecting the whole people is to
        be irrevocably fixed by decisions of the Supreme Court, . . . the people will have ceased to be their own
        rulers, having to that extent practically resigned their Government into the hands of that eminent tribunal.\"
        A. Lincoln, First Inaugural Address (Mar. 4, 1861), reprinted in Inaugural Addresses of the Presidents of the
        United States, S. Doc. No. 101-10, p. 139 (1989).</blockquote>\n<p>It is particularly difficult, in the
        circumstances of the present decision, to sit still for the Court's lengthy lecture upon the virtues of
        \"constancy,\" <i>ante,</i> at 868, of \"remain[ing] steadfast,\" <i>ibid.,</i> and adhering to \"principle,\"
        <i>ante, passim.</i> Among the five Justices who purportedly adhere to <i>Roe,</i> at most three agree upon the
        <i>principle</i> that constitutes adherence (the joint opinion's \"undue burden\" standard)and that principle
        is inconsistent with <i>Roe.</i> See 410 U. S., at 154-156.<sup>[7]</sup> To make matters worse, two of the
        three, in order thus to remain steadfast, had to abandon previously stated positions. See n. 4, <i>supra;</i>
        see <i>supra,</i> at 988-990. It is beyond me how the Court expects these accommodations to be accepted \"as
        grounded truly in principle, not as compromises with social and political pressures having, as such, no bearing
        on the principled choices that the Court is obliged to make.\" <i>Ante,</i> at 865-866. The only principle the
        Court \"adheres\" <span class=\"star-pagination\">*998</span> to, it seems to me, is the principle that the
        Court must be seen as standing by <i>Roe.</i> That is not a principle of law (which is what I thought the Court
        was talking about), but a principle of <i>Realpolitik</i>and a wrong one at that.
    </p>\n<p>I cannot agree with,
        indeed I am appalled by, the Court's suggestion that the decision whether to stand by an erroneous
        constitutional decision must be strongly influenced <i>against</i> overruling, no lessby the substantial and
        continuing public opposition the decision has generated. The Court's judgment that any other course would
        \"subvert the Court's legitimacy\" must be another consequence of reading the error-filled history book that
        described the deeply divided country brought together by <i>Roe.</i> In my history book, the Court was covered
        with dishonor and deprived of legitimacy by <i>Dred Scott</i> v. <i>Sandford,</i> 19 How. 393 (1857), an
        erroneous (and widely opposed) opinion that it did not abandon, rather than by <i>West Coast Hotel Co.</i> v.
        <i>Parrish,</i> 300 U. S. 379 (1937), which produced the famous \"switch in time\" from the Court's erroneous
        (and widely opposed) constitutional opposition to the social measures of the New Deal. (Both <i>Dred Scott</i>
        and one line of the cases resisting the New Deal rested upon the concept of \"substantive due process\" that the
        Court praises and employs today. Indeed, <i>Dred Scott</i> was \"very possibly the first application of
        substantive due process in the Supreme Court, the original precedent for <i>Lochner</i> v. <i>New York</i> and
        <i>Roe</i> v. <i>Wade</i><i>.</i> \" D. Currie, The Constitution in the Supreme Court 271 (1985) (footnotes
        omitted).)
    </p>\n<p>But whether it would \"subvert the Court's legitimacy\" or not, the notion that we would
        decide a case differently from the way we otherwise would have in order to show that we can stand firm against
        public disapproval is frightening. It is a bad enough idea, even in the head of someone like me, who believes
        that the text of the Constitution, and our traditions, say what they say and there is no fiddling with them. But
        when it is in the mind of a Court that believes the Constitution <span class=\"star-pagination\">*999</span> has
        an evolving meaning, see <i>ante,</i> at 848; that the Ninth Amendment's reference to \"othe[r]\" rights is not
        a disclaimer, but a charter for action, <i>ibid.;</i> and that the function of this Court is to \"speak before
        all others for [the people's] constitutional ideals\" unrestrained by meaningful text or traditionthen the
        notion that the Court must adhere to a decision for as long as the decision faces \"great opposition\" and the
        Court is \"under fire\" acquires a character of almost czarist arrogance. We are offended by these marchers who
        descend upon us, every year on the anniversary of <i>Roe,</i> to protest our saying that the Constitution
        requires what our society has never thought the Constitution requires. These people who refuse to be \"tested by
        following\" must be taught a lesson. We have no Cossacks, but at least we can stubbornly refuse to abandon an
        erroneous opinion that we might otherwise changeto show how little they intimidate us.</p>\n<p>Of course, as
        The Chief Justice points out, we have been subjected to what the Court calls \"`political pressure' \" by
        <i>both</i> sides of this issue. <i>Ante,</i> at 963. Maybe today's decision <i>not</i> to overrule <i>Roe</i>
        will be seen as buckling to pressure from <i>that</i> direction. Instead of engaging in the hopeless task of
        predicting public perceptiona job not for lawyers but for political campaign managersthe Justices should do
        what is <i>legally</i> right by asking two questions: (1) Was <i>Roe</i> correctly decided? (2) Has <i>Roe</i>
        succeeded in producing a settled body of law? If the answer to both questions is no, <i>Roe</i> should
        undoubtedly be overruled.
    </p>\n<p>In truth, I am as distressed as the Court isand expressed my distress several
        years ago, see <i>Webster,</i> 492 U. S., at 535about the \"political pressure\" directed to the Court: the
        marches, the mail, the protests aimed at inducing us to change our opinions. How upsetting it is,that so many of
        our citizens (good people, not lawless ones, on both sides of this abortion issue, and on various sides of other
        issues as well) think that we Justices should properly take into account <span
            class=\"star-pagination\">*1000</span> their views, as though we were engaged not in ascertaining an
        objective law but in determining some kind of social consensus. The Court would profit, I think, from giving
        less attention to the <i>fact</i> of this distressing phenomenon, and more attention to the <i>cause</i> of it.
        That cause permeates today's opinion: a new mode of constitutional adjudication that relies not upon text and
        traditional practice to determine the law, but upon what the Court calls \"reasoned judgment,\" <i>ante,</i> at
        849, which turns out to be nothing but philosophical predilection and moral intuition. All manner of
        \"liberties,\" the Court tells us, inhere in the Constitution and are enforceable by this Courtnot just those
        mentioned in the text or established in the traditions of our society. <i>Ante,</i> at 847-849. Why even the
        Ninth Amendmentwhich says only that \"[t]he enumeration in the Constitution, of certain rights, shall not be
        construed to deny or disparage others retained by the people\"is, despite our contrary understanding for almost
        200 years, a literally boundless source of additional, unnamed, unhinted-at \"rights,\" definable and
        enforceable by us, through \"reasoned judgment.\" <i>Ante,</i> at 848-849.</p>\n<p>What makes all this relevant
        to the bothersome application of \"political pressure\" against the Court are the twin facts that the American
        people love democracy and the American people are not fools. As long as this Court thought (and the people
        thought) that we Justices were doing essentially lawyers' work up herereading text and discerning our society's
        traditional understanding of that textthe public pretty much left us alone. Texts and traditions are facts to
        study, not convictions to demonstrate about. But if in reality our process of constitutional adjudication
        consists primarily of making <i>value judgments;</i> if we can ignore a long and clear tradition clarifying an
        ambiguous text, as we did, for example, five days ago in declaring unconstitutional invocations and benedictions
        at public high school graduation ceremonies, <i>Lee</i> v. <i>Weisman,</i> 505 U. S. 577 (1992); if, as I say,
        our pronouncement of constitutional law rests primarily on value <span class=\"star-pagination\">*1001</span>
        judgments, then a free and intelligent people's attitude towards us can be expected to be (<i>ought</i> to be)
        quite different. The people know that their value judgments are quite as good as those taught in any law
        schoolmaybe better. If, indeed, the \"liberties\" protected by the Constitution are, as the Court says,
        undefined and unbounded, then the people <i>should</i> demonstrate, to protest that we do not implement
        <i>their</i> values instead of <i>ours.</i> Not only that, but confirmation hearings for new Justices
        <i>should</i> deteriorate into questionand-answer sessions in which Senators go through a list of their
        constituents' most favored and most disfavored alleged constitutional rights, and seek the nominee's commitment
        to support or oppose them. Value judgments, after all, should be voted on, not dictated; and if our Constitution
        has somehow accidently committed them to the Supreme Court, at least we can have a sort of plebiscite each time
        a new nominee to that body is put forward. Justice Blackmun not only regards this prospect with equanimity, he
        solicits it. <i>Ante,</i> at 943.
    </p>\n<p></p>\n<h2>* * *</h2>\n<p>There is a poignant aspect to today's
        opinion. Its length, and what might be called its epic tone, suggest that its authors believe they are bringing
        to an end a troublesome era in the history of our Nation and of our Court. \"It is the dimension\" of authority,
        they say, to \"cal[l] the contending sides of national controversy to end their national division by accepting a
        common mandate rooted in the Constitution.\" <i>Ante,</i> at 867.</p>\n<p>There comes vividly to mind a portrait
        by Emanuel Leutze that hangs in the Harvard Law School: Roger Brooke Taney, painted in 1859, the 82d year of his
        life, the 24th of his Chief Justiceship, the second after his opinion in <i>Dred Scott.</i> He is all in black,
        sitting in a shadowed red armchair, left hand resting upon a pad of paper in his lap, right hand hanging limply,
        almost lifelessly, beside the inner arm of the chair. He sits facing the viewer and staring straight out. There
        <span class=\"star-pagination\">*1002</span> seems to be on his face, and in his deep-set eyes, an expression of
        profound sadness and disillusionment. Perhaps he always looked that way, even when dwelling upon the happiest of
        thoughts. But those of us who know how the lustre of his great Chief Justiceship came to be eclipsed by <i>Dred
            Scott</i> cannot help believing that he had that caseits already apparent consequences for the Court and
        its soon-to-beplayed-out consequences for the Nationburning on his mind. I expect that two years earlier he,
        too, had thought himself \"call[ing] the contending sides of national controversy to end their national division
        by accepting a common mandate rooted in the Constitution.\"
    </p>\n<p>It is no more realistic for us in this
        litigation, than it was for him in that, to think that an issue of the sort they both involvedan issue
        involving life and death, freedom and subjugationcan be \"speedily and finally settled\" by the Supreme Court,
        as President James Buchanan in his inaugural address said the issue of slavery in the territories would be. See
        Inaugural Addresses of the Presidents of the United States, S. Doc. No. 101-10, p. 126 (1989). Quite to the
        contrary, by foreclosing all democratic outlet for the deep passions this issue arouses, by banishing the issue
        from the political forum that gives all participants, even the losers, the satisfaction of a fair hearing and an
        honest fight, by continuing the imposition of a rigid national rule instead of allowing for regional
        differences, the Court merely prolongs and intensifies the anguish.</p>\n<p>We should get out of this area,
        where we have no right to be, and where we do neither ourselves nor the country any good by remaining.</p>\n<h2>
        NOTES</h2>\n<p>[*] Together with No. 91-902, <i>Casey, Governor of Pennsylvania, et al.</i> v. <i>Planned
            Parenthood of Southeastern Pennsylvania et al.,</i> also on certiorari to the same court.</p>\n<p>[] Briefs
        of <i>amici curiae</i> were filed for the State of New York et al. by <i>Robert Abrams,</i> Attorney General of
        New York, <i>Jerry Boone,</i> Solicitor General, <i>Mary Ellen Burns,</i> Chief Assistant Attorney General, and
        <i>Sanford M. Cohen, Donna I. Dennis, Marjorie Fujiki,</i> and <i>Shelley B. Mayer,</i> Assistant Attorneys
        General, and <i>John McKernan,</i> Governor of Maine, and <i>Michael E. Carpenter,</i> Attorney General,
        <i>Richard Blumenthal,</i> Attorney General of Connecticut, <i>Charles M. Oberly III,</i> Attorney General of
        Delaware, <i>Warren Price III,</i> Attorney General of Hawaii, <i>Roland W. Burris,</i> Attorney General of
        Illinois, <i>Bonnie J. Campbell,</i> Attorney General of Iowa, <i>J. Joseph Curran, Jr.,</i> Attorney General of
        Maryland, <i>Scott Harshbarger,</i> Attorney General of Massachusetts, <i>Frankie Sue Del Papa,</i> Attorney
        General of Nevada, <i>Robert J. Del Tufo,</i> Attorney General of New Jersey, <i>Tom Udall,</i> Attorney General
        of New Mexico<i>, Lacy H. Thornburg,</i> Attorney General of North Carolina, <i>James E. O'Neil,</i> Attorney
        General of Rhode Island, <i>Dan Morales,</i> Attorney General of Texas, <i>Jeffrey L. Amestoy,</i> Attorney
        General of Vermont, and <i>John Payton,</i> Corporation Counsel of District of Columbia; for the State of Utah
        by <i>R. Paul Van Dam,</i> Attorney General, and <i>Mary Anne Q. Wood,</i> Special Assistant Attorney General;
        for the City of New York et al. by <i>O. Peter Sherwood, Conrad Harper, Janice Goodman, Leonard J. Koerner,
            Lorna Bade Goodman, Gail Rubin,</i> and <i>Julie Mertus;</i> for 178 Organizations by <i>Pamela S.</i>
        <i>Karlan</i> and <i>Sarah Weddington;</i> for Agudath Israel of America by <i>David Zwiebel;</i> for the Alan
        Guttmacher Institute et al. by <i>Colleen K. Connell</i> and <i>Dorothy B. Zimbrakos;</i> for the American
        Academy of Medical Ethics by <i>Joseph W. Dellapenna;</i> for the American Association of Prolife Obstetricians
        and Gynecologists et al. by <i>William Bentley Ball, Philip J. Murren,</i> and <i>Maura K. Quinlan;</i> for the
        American College of Obstetricians and Gynecologists et al. by <i>Carter G. Phillips, Ann E. Allen, Laurie R.
            Rockett, Joel I. Klein, Nadine Taub,</i> and <i>Sarah C. Carey;</i> for the American Psychological
        Association by <i>David W. Ogden;</i> for Texas Black Americans for Life by <i>Lawrence J. Joyce</i> and
        <i>Craig H. Greenwood;</i> for Catholics United for Life et al. by <i>Thomas Patrick Monaghan, Jay Alan Sekulow,
            Walter M. Weber, Thomas A. Glessner, Charles E. Rice,</i> and <i>Michael J. Laird;</i> for the Elliot
        Institute for Social Sciences Research by <i>Stephen R. Kaufmann;</i> for Feminists for Life of America et al.
        by <i>Keith A. Fournier, John G. Stepanovich, Christine Smith Torre, Theodore H. Amshoff, Jr.,</i> and <i>Mary
            Dice Grenen;</i> for Focus on the Family et al. by <i>Stephen H. Galebach, Gregory J. Granitto, Stephen W.
            Reed, David L. Llewellyn, Jr., Benjamin W. Bull,</i> and <i>Leonard J. Pranschke;</i> for the Knights of
        Columbus by <i>Carl A. Anderson;</i> for the Life Issues Institute by <i>James Bopp, Jr.,</i> and <i>Richard E.
            Coleson;</i> for the NAACP Legal Defense and Educational Fund, Inc., et al. by <i>Julius L. Chambers, Ronald
            L. Ellis,</i> and <i>Alice L. Brown;</i> for the National Legal Foundation by <i>Robert K. Skolrood;</i> for
        National Right to Life, Inc., by Messrs. Bopp and Coleson, <i>Robert A. Destro,</i> and <i>A. Eric Johnston;</i>
        for the Pennsylvania Coalition Against Domestic Violence et al. by <i>Phyllis Gelman;</i> for the Rutherford
        Institute et al. by <i>Thomas W. Strahan, John W. Whitehead, Mr. Johnston, Stephen E. Hurst, Joseph Secola,
            Thomas S. Neuberger, J. Brian Heller, Amy Dougherty, Stanley R. Jones, David Melton, Robert R. Melnick,
            William Bonner, W. Charles Bundren,</i> and <i>James Knicely;</i> for the Southern Center for Law &amp;
        Ethics by <i>Tony G. Miller;</i> for the United States Catholic Conference et al. by <i>Mark E. Chopko, Phillip
            H. Harris, Michael K. Whitehead,</i> and <i>Forest D. Montgomery;</i> for University Faculty for Life by
        <i>Clarke D. Forsythe</i> and <i>Victor G. Rosenblum;</i> for Certain American State Legislators by <i>Paul
            Benjamin Linton;</i> for 19 Arizona Legislators by <i>Ronald D. Maines;</i> for Representative Henry J. Hyde
        et al. by <i>Albert P. Blaustein</i> and <i>Kevin J. Todd;</i> for Representative Don Edwards et al. by
        <i>Walter Dellinger</i> and <i>Lloyd N. Cutler;</i> and for 250 American Historians by <i>Sylvia A. Law.</i>
    </p>\n<p>[1] It is sometimes useful to view the issue of <i>stare decisis</i> from a historical perspective. In the
        last 19 years, 15 Justices have confronted the basic issue presented in <i>Roe</i> v.<i>Wade,</i> 410 U. S. 113
        (1973). Of those, 11 have voted as the majority does today: Chief Justice Burger, Justices Douglas, Brennan,
        Stewart, Marshall, and Powell, and Justices Blackmun, O'Connor, Kennedy, Souter, and myself. Only fourall of
        whom happen to be on the Court todayhave reached the opposite conclusion.</p>\n<p>[2] Professor Dworkin has
        made this comment on the issue:\n</p>\n<p>\"The suggestion that states are free to declare a fetus a person. . .
        . assumes that a state can curtail some persons' constitutional rights by adding new persons to the
        constitutional population. The constitutional rights of one citizen are of course very much affected by who or
        what else also has constitutional rights, because the rights of others may compete or conflict with his. So any
        power to increase the constitutional population by unilateral decision would be, in effect, a power to decrease
        rights the national Constitution grants to others.</p>\n<p>\". . . If a state could declare trees to be persons
        with a constitutional right to life, it could prohibit publishing newspapers or books in spite of the First
        Amendment's guarantee of free speech, which could not be understood as a license to kill. . . . Once we
        understand that the suggestion we are considering has that implication, we must reject it. If a fetus is not
        part of the constitutional population, under the national constitutional arrangement, then states have no power
        to overrule that national arrangement by themselves declaring that fetuses have rights competitive with the
        constitutional rights of pregnant women.\" Unenumerated Rights: Whether and How <i>Roe</i> Should be Overruled,
        59 U. Chi. L. Rev. 381, 400 401 (1992).</p>\n<p>[3] The state interest in protecting potential life may be
        compared to the state interest in protecting those who seek to immigrate to this country. A contemporary example
        is provided by the Haitians who have risked the perils of the sea in a desperate attempt to become \"persons\"
        protected by our laws. Humanitarian and practical concerns would support a state policy allowing those persons
        unrestricted entry; countervailing interests in population control support a policy of limiting the entry of
        these potential citizens. While the state interest in population control might be sufficient to justify strict
        enforcement of the immigration laws, that interest would not be sufficient to overcome a woman's liberty
        interest. Thus, a state interest in population control could not justify a state-imposed limit on family size
        or, for that matter, state-mandated abortions.</p>\n<p>[4] As we noted in that opinion, the State's \"legitimate
        interest in protecting minor women from their own immaturity\" distinguished that case from <i>Akron</i> v.
        <i>Akron Center for Reproductive Health, Inc.,</i> 462 U. S. 416 (1983), which involved \"a provision that
        required that mature women, capable of consenting to an abortion, wait 24 hours after giving consent before
        undergoing an abortion.\" <i>Hodgson,</i> 497 U. S., at 449, n. 35.
    </p>\n<p>[5] The joint opinion's reliance on
        the indirect effects of the regulation of constitutionally protected activity, see <i>ante,</i> at 873-874, is
        misplaced; what matters is not only the effect of a regulation but also the reason for the regulation. As I
        explained in <i>Hodgson:</i>\n</p>\n<p>\"In cases involving abortion, as in cases involving the right to travel
        or the right to marry, the identification of the constitutionally protected interest is merely the beginning of
        the analysis. State regulation of travel and of marriage is obviously permissible even though a State may not
        categorically exclude nonresidents from its borders, <i>Shapiro</i> v. <i>Thompson,</i> 394 U. S. 618, 631
        (1969), or deny prisoners the right to marry, <i>Turner</i> v. <i>Safley,</i> 482 U. S. 78, 94-99 (1987). But
        the regulation of constitutionally protected decisions, such as where a person shall reside or whom he or she
        shall marry, must be predicated on legitimate state concerns other than disagreement with the choice the
        individual has made. Cf. <i>Turner</i> v. <i>Safley, supra</i><i>; </i><i>Loving</i> v. <i>Virginia,</i> 388 U.
        S. 1, 12 (1967). In the abortion area, a State may have no obligation to spend its own money, or use its own
        facilities, to subsidize nontherapeutic abortions for minors or adults. See, <i>e. g., </i><i>Maher</i> v.
        <i>Roe,</i> 432 U. S. 464 (1977); cf. <i>Webster</i> v. <i>Reproductive</i> <i>Health Services,</i> 492 U. S.
        490, 508-511 (1989); <i>id.,</i> at 523-524 (O'Connor, J., concurring in part and concurring in judgment). A
        State's value judgment favoring childbirth over abortion may provide adequate support for decisions involving
        such allocation of public funds, but not for simply substituting a state decision for an individual decision
        that a woman has a right to make for herself. Otherwise, the interest in liberty protected by the Due Process
        Clause would be a nullity. A state policy favoring childbirth over abortion is not in itself a sufficient
        justification for overriding the woman's decision or for placing `obstaclesabsolute or otherwisein the
        pregnant woman's path to an abortion.' \" 497 U. S., at 435.
    </p>\n<p>[6] The meaning of any legal standard can
        only be understood by reviewing the actual cases in which it is applied. For that reason, I discount both
        Justice Scalia's comments on past descriptions of the standard, see <i>post,</i> at 988-990 (opinion concurring
        in judgment in part and dissenting in part), and the attempt to give it crystal clarity in the joint opinion.
        The several opinions supporting the judgment in <i>Griswold</i> v. <i>Connecticut,</i> 381 U. S. 479 (1965), are
        less illuminating than the central holding of the case, which appears to have passed the test of time. The
        future may also demonstrate that a standard that analyzes both the severity of a regulatory burden and the
        legitimacy of its justification will provide a fully adequate framework for the review of abortion legislation
        even if the contours of the standard are not authoritatively articulated in any single opinion.</p>\n<p>[7] U.
        S. Dept. of Commerce, Bureau of the Census, Statistical Abstract of the United States 71 (111th ed. 1991).</p>\n
    <p>[8] Although I agree that a parental-consent requirement (with the appropriate bypass) is constitutional, I do
        not join Part VD of the joint opinion because its approval of Pennsylvania's informed parental-consent
        requirement is based on the reasons given in Part VB, with which I disagree.</p>\n<p>[1] As I shall explain,
        the joint opinion and I disagree on the appropriate standard of review for abortion regulations. I do agree,
        however, that the reasons advanced by the joint opinion suffice to invalidate the spousal notification
        requirement under a strict scrutiny standard.</p>\n<p>[2] I also join the Court's decision to uphold the medical
        emergency provision. As the Court notes, its interpretation is consistent with the essential holding
        of<i>Roe</i> that \"forbids a State to interfere with a woman's choice to undergo an abortion procedure if
        continuing her pregnancy would constitute a threat to her health.\" <i>Ante,</i> at 880. As is apparent in my
        analysis below, however, this exception does not render constitutional the provisions which I conclude do not
        survive strict scrutiny.</p>\n<p>[3] As the joint opinion acknowledges, <i>ante,</i> at 857, this Court has
        recognized the vital liberty interest of persons in refusing unwanted medical treatment. <i>Cruzan</i> v.
        <i>Director, Mo. Dept. of Health,</i> 497 U. S. 261 (1990). Just as the Due Process Clause protects the deeply
        personal decision of the individual to <i>refuse</i> medical treatment, it also must protect the deeply personal
        decision to <i>obtain</i> medical treatment, including a woman's decision to terminate a pregnancy.
    </p>\n<p>[4]
        A growing number of commentators are recognizing this point. See, <i>e. g.,</i> L. Tribe, American
        Constitutional Law § 15-10, pp. 1353-1359 (2d ed. 1988); Siegel, Reasoning from the Body: A Historical
        Perspective on Abortion Regulation and Questions of Equal Protection, 44 Stan. L. Rev. 261, 350-380 (1992);
        Sunstein, Neutrality in Constitutional Law (With Special Reference to Pornography, Abortion, and Surrogacy), 92
        Colum. L. Rev. 1, 31-44 (1992); cf. Rubenfeld, The Right of Privacy, 102 Harv. L. Rev. 737, 788-791 (1989)
        (similar analysis under the rubric of privacy); MacKinnon, Reflections on Sex Equality Under Law, 100 Yale L. J.
        1281, 1308-1324 (1991).</p>\n<p>[5] To say that restrictions on a right are subject to strict scrutiny is not to
        say that the right is absolute. Regulations can be upheld if they have no significant impact on the woman's
        exercise of her right and are justified by important state health objectives. See, <i>e. g., </i><i>Planned
            Parenthood of Central Mo.</i> v. <i>Danforth,</i> 428 U. S. 52, 65-67, 79-81 (1976) (upholding requirements
        of a woman's written consent and record keeping). But the Court today reaffirms the essential principle of
        <i>Roe</i> that a woman has the right \"to choose to have an abortion before viability and to obtain it without
        undue interference from the State.\" <i>Ante,</i> at 846. Under <i>Roe,</i> any more than <i>de minimis</i>
        interference is undue.
    </p>\n<p>[6] The joint opinion agrees with <i>Roe</i>`s conclusion that viability occurs
        at 23 or 24 weeks at the earliest. Compare <i>ante,</i> at 860, with <i>Roe</i> v. <i>Wade,</i> 410 U. S. 113,
        160 (1973).</p>\n<p>[7] While I do not agree with the joint opinion's conclusion that these provisions should be
        upheld, the joint opinion has remained faithful to principles this Court previously has announced in examining
        counseling provisions. For example, the joint opinion concludes that the \"information the State requires to be
        made available to the woman\" must be \"truthful and not misleading.\" <i>Ante,</i> at 882. Because the State's
        information must be \"calculated to inform the woman's free choice, not hinder it,\" <i>ante,</i> at 877, the
        measures must be designed to ensure that a woman's choice is \"mature and informed,\" <i>ante,</i> at 883, not
        intimidated, imposed, or impelled. To this end, when the State requires the provision of certain information,
        the State may not alter the <i>manner</i> of presentation in order to inflict \"psychological abuse,\"
        <i>ante,</i> at 893, designed to shock or unnerve a woman seeking to exercise her liberty right. This, for
        example, would appear to preclude a State from requiring a woman to view graphic literature or films detailing
        the performance of an abortion operation. Just as a visual preview of an operation to remove an appendix plays
        no part in a physician's securing informed consent to an appendectomy, a preview of scenes appurtenant to any
        major medical intrusion into the human body does not constructively inform the decision of a woman of the
        State's interest in the preservation of the woman's health or demonstrate the State's \"profound respect for the
        life of the unborn.\" <i>Ante,</i> at 877.
    </p>\n<p>[8] The Court's decision in <i>Hodgson</i> v.
        <i>Minnesota,</i> 497 U. S. 417 (1990), validating a 48-hour waiting period for minors seeking an abortion to
        permit parental involvement does not alter this conclusion. Here the 24-hour delay is imposed on an <i>adult</i>
        woman. See <i>id.,</i> at 449-450, n. 35; <i>Ohio</i> v. <i>Akron Center for Reproductive Health, Inc.,</i> 497
        U. S. 502 (1990). Moreover, the statute in <i>Hodgson</i> did not require any delay once the minor obtained the
        affirmative consent of either a parent or the court.
    </p>\n<p>[9] Because this information is so widely known, I
        am confident that a developed record can be made to show that the 24-hour delay, \"in a large fraction of the
        cases in which [the restriction] is relevant, . . . will operate as a substantial obstacle to a woman's choice
        to undergo an abortion.\" <i>Ante,</i> at 895.</p>\n<p>[10] The judicial-bypass provision does not cure this
        violation.<i>Hodgson</i> is distinguishable, since these cases involve more than parental involvement or
        approvalrather, the Pennsylvania law requires that the parent receive information designed to discourage
        abortion in a face-to-face meeting with the physician. The bypass procedure cannot ensure that the parent would
        obtain the information, since in many instances, the parent would not even attend the hearing. A State may not
        place any restriction on a young woman's right to an abortion,however irrational,simply because it has provided
        a judicial bypass.</p>\n<p>[11] Obviously, I do not share The Chief Justice's views of homosexuality as sexual
        deviance. See <i>Bowers,</i> 478 U. S., at 202-203, n. 2.</p>\n<p>[12] Justice Scalia urges the Court to \"get
        out of this area,\" <i>post,</i> at 1002, and leave questions regarding abortion entirely to the States,
        <i>post,</i> at 999-1000. Putting aside the fact that what he advocates is nothing short of an abdication by the
        Court of its constitutional responsibilities, Justice Scalia is uncharacteristically naive if he thinks that
        overruling <i>Roe</i> and holding that restrictions on a woman's right to an abortion are subject only to
        rational-basis review will enable the Court henceforth to avoid reviewing abortion-related issues. State efforts
        to regulate and prohibit abortion in a post-<i>Roe</i> world undoubtedly would raise a host of distinct and
        important constitutional questions meriting review by this Court. For example, does the Eighth Amendment impose
        any limits on the degree or kind of punishment a State can inflict upon physicians who perform, or women who
        undergo, abortions? What effect would differences among States in their approaches to abortion have on a woman's
        right to engage in interstate travel? Does the First Amendment permit States that choose not to criminalize
        abortion to ban all advertising providing information about where and how to obtain abortions?
    </p>\n<p>[1] Two
        years after <i>Roe,</i> the West German constitutional court, by contrast, struck down a law liberalizing access
        to abortion on the grounds that life developing within the womb is constitutionally protected. <i>Judgment of
            February 25, 1975,</i> 39 BVerfGE 1 (translated in Jonas &amp; Gorby, West German Abortion Decision: A
        Contrast to <i>Roe</i> v. <i>Wade</i><i>,</i> 9 John Marshall J. Prac. &amp; Proc. 605 (1976)). In 1988, the
        Canadian Supreme Court followed reasoning similar to that of <i>Roe</i> in striking down a law that restricted
        abortion. <i>Morgentaler</i> v. <i>Queen,</i> 1 S. C. R. 30, 44 D. L. R. 4th 385 (1988).</p>\n<p>[2] The joint
        opinion of Justices O'Connor, Kennedy, and Souter appears to ignore this point in concluding that the spousal
        notice provision imposes an undue burden on the abortion decision. <i>Ante,</i> at 887-898. In most instances
        the notification requirement operates without difficulty. As the District Court found, the vast majority of
        wives seeking abortions notify and consult with their husbands, and thus suffer no burden as a result of the
        provision. 744 F. Supp. 1323, 1360 (ED Pa. 1990). In other instances where a woman does not want to notify her
        husband, the Act provides exceptions. For example, notification is not required if the husband is not the
        father, if the pregnancy is the result of a reported spousal sexual assault, or if the woman fears bodily injury
        as a result of notifying her husband. Thus, in these instances as well, the notification provision imposes no
        obstacle to the abortion decision.\n</p>\n<p>The joint opinion puts to one side these situations where the
        regulation imposes no obstacle at all,and instead focuses on the group of married women who would not otherwise
        notify their husbands and who do not qualify for one of the exceptions. Having narrowed the focus, the joint
        opinion concludes that in a \"large fraction\" of those cases, the notification provision operates as a
        substantial obstacle, <i>ante,</i> at 895, and that the provision is therefore invalid. There are certainly
        instances where a woman would prefer not to notify her husband, and yet does not qualify for an exception. For
        example, there are the situations of battered women who fear psychological abuse or injury to their children as
        a result of notification; because in these situations the women do not fear bodily injury, they do not qualify
        for an exception. And there are situations where a woman has become pregnant as a result of an unreported
        spousal sexual assault; when such an assault is unreported, no exception is available. But, as the District
        Court found, there are also instances where the woman prefers not to notify her husband for a variety of other
        reasons. See 744 F. Supp., at 1360. For example, a woman might desire to obtain an abortion without her
        husband's knowledge because of perceived economic constraints or her husband's previously expressed opposition
        to abortion. The joint opinion concentrates on the situations involving battered women and unreported spousal
        assault, and assumes, without any support in the record, that these instances constitute a \"large fraction\" of
        those cases in which women prefer not to notify their husbands (and do not qualify for an exception).
        <i>Ante,</i> at 895. This assumption is not based on any hard evidence, however. And were it helpful to an
        attempt to reach a desired result, one could just as easily assume that the battered women situations form 100
        percent of the cases where women desire not to notify, or that they constitute only 20 percent of those cases.
        But reliance on such speculation is the necessary result of adopting the undue burden standard.
    </p>\n<p>[3] The
        definition in use at that time provided as follows:\n</p>\n<p>\"`Medical emergency.'That condition which, on the
        basis of the physician's best clinical judgment, so complicates a pregnancy as to necessitate the immediate
        abortion of same to avert the death of the mother or for which a 24-hour delay will create grave peril of
        immediate and irreversible loss of major bodily function.\" Pa. Stat.Ann., Tit.18, § 3203(Purdon 1983).</p>\n<p>
        [1] The Court's suggestion, <i>ante,</i> at 847-848, that adherence to tradition would require us to uphold laws
        against interracial marriage is entirely wrong. Any tradition in that case was contradicted <i>by a text</i> an
        Equal Protection Clause that explicitly establishes racial equality as a constitutional value. See <i>Loving</i>
        v. <i>Virginia,</i> 388 U. S. 1, 9 (1967) (\"In the case at bar, . . . we deal with statutes containing racial
        classifications, and the fact of equal application does not immunize the statute from the very heavy burden of
        justification which the Fourteenth Amendment has traditionally required of state statutes drawn according to
        race\"); see also <i>id.,</i> at 13 (Stewart, J., concurring in judgment). The enterprise launched in <i>Roe</i>
        v. <i>Wade,</i> 410 U. S. 113 (1973), by contrast, sought to <i>establish</i> in the teeth of a clear, contrary
        traditiona value found nowhere in the constitutional text.\n</p>\n<p>There is, of course, no comparable
        tradition barring recognition of a \"liberty interest\" in carrying one's child to term free from state efforts
        to kill it. For that reason, it does not follow that the Constitution does not protect childbirth simply because
        it does not protect abortion. The Court's contention, <i>ante,</i> at 859, that the only way to protect
        childbirth is to protect abortion shows the utter bankruptcy of constitutional analysis deprived of tradition as
        a validating factor.It drives one to say that the only way to protect the right to eat is to acknowledge the
        constitutional right to starve oneself to death.</p>\n<p>[2] Justice Blackmun's parade of adjectives is
        similarly empty: Abortion is among \"`the most intimate and personal choices,' \"<i>ante,</i> at 923; it is a
        matter \"central to personal dignity and autonomy,\" <i>ibid.;</i> and it involves \"personal decisions that
        profoundly affect bodily integrity,identity,and destiny,\" <i>ante,</i> at 927.Justice Stevens is not much less
        conclusory: The decision to choose abortion is a matter of \"the highest privacy and the most personal nature,\"
        <i>ante,</i> at 915; it involves a \"`difficult choice having serious and personal consequences of major
        importance to [a woman's] future,' \" <i>ante,</i> at 916; the authority to make this \"traumatic and yet
        empowering decisio[n]\" is \"an element of basic human dignity,\" <i>ibid.;</i> and it is \"nothing less than a
        matter of conscience,\" <i>ibid.</i>
    </p>\n<p>[3] The joint opinion is clearly wrong in asserting, <i>ante,</i>
        at 874, that \"the Court's early abortion cases adhered to\" the \"undue burden\" standard. The passing use of
        that phrase in Justice Blackmun's opinion for the Court in <i>Bellotti</i> v. <i>Baird,</i> 428 U. S. 132, 147
        (1976) <i>(Bellotti I)</i><i>,</i> was not by way of setting forth the <i>standard</i> of unconstitutionality,
        as Justice O'Connor's later opinions did, but by way of expressing the <i>conclusion</i> of unconstitutionality.
        Justice Powell for a time appeared to employ a variant of \"undue burden\" analysis in several non majority
        opinions, see, <i>e. g., </i><i>Bellotti</i> v. <i>Baird,</i> 443 U. S. 622, 647 (1979) <i>(Bellotti II)</i><i>;
        </i><i>Carey</i> v. <i>Population Services International,</i> 431 U. S. 678, 705 (1977) (opinion concurring in
        part and concurring in judgment), but he too ultimately rejected that standard in his opinion for the Court in
        <i>Akron</i> v. <i>Akron Center for Reproductive Health, Inc.,</i> 462 U. S. 416, 420, n. 1 (1983) <i>(Akron
            I)</i> . The joint opinion's reliance on <i>Maher</i> v. <i>Roe,</i> 432 U. S. 464, 473 (1977), and
        <i>Harris</i> v. <i>McRae,</i> 448 U. S. 297, 314 (1980), is entirely misplaced, since those cases did not
        involve regulation of abortion, but mere refusal to fund it. In any event, Justice O'Connor's earlier
        formulations have apparently now proved unsatisfactory to the three Justices, whoin the name of <i>stare
            decisis</i> no lesstoday find it necessary to devise an entirely new version of \"undue burden\" analysis.
        See <i>ante,</i> at 877-879.
    </p>\n<p>[4] The joint opinion further asserts that a law imposing an undue burden
        on abortion decisions is not a \"permissible\" means of serving \"legitimate\" state interests. <i>Ante,</i> at
        877. This description of the undue burden standard in terms more commonly associated with the rational-basis
        test will come as a surprise even to those who have followed closely our wanderings in this forsaken wilderness.
        See, <i>e. g., </i><i>Akron I, supra,</i> at 463 (O'Connor, J., dissenting) (\"The `undue burden' . . .
        represents the required threshold inquiry that must be conducted before this Court can require a State to
        justify its legislative actions under the exacting `compelling state interest' standard\"); see also
        <i>Hodgson</i> v. <i>Minnesota,</i> 497 U. S. 417, 458-460 (1990) (O'Connor, J., concurring in part and
        concurring in judgment in part); <i>Thornburgh</i> v. <i>American College of Obstetricians and
            Gynecologists,</i> 476 U. S. 747, 828 (1986) (O'Connor, J., dissenting). This confusing equation of the two
        standards is apparently designed to explain how one of the Justices who joined the plurality opinion in
        <i>Webster</i> v. <i>Reproductive Health Services,</i> 492 U. S. 490 (1989), which adopted the rational-basis
        test, could join an opinion expressly adopting the undue burden test. See <i>id.,</i> at 520 (rejecting the view
        that abortion is a \"fundamental right,\" instead inquiring whether a law regulating the woman's \"liberty
        interest\" in abortion is \"reasonably designed\" to further \"legitimate\" state ends). The same motive also
        apparently underlies the joint opinion's erroneous citation of the plurality opinion in <i>Ohio</i> v. <i>Akron
            Center for Reproductive Health,</i> 497 U. S. 502, 506 (1990) <i>(Akron II)</i> (opinion of Kennedy, J.), as
        applying the undue burden test. See <i>ante,</i> at 876 (using this citation to support the proposition that
        \"two of us\"<i>i. e.,</i> two of the authors of the joint opinionhave previously applied this test). In fact,
        <i>Akron II</i> does not mention the undue burden standard until the conclusion of the opinion, when it states
        that the statute at issue \"does not impose an undue, <i>or otherwise unconstitutional,</i> burden.\" 497 U. S.,
        at 519 (emphasis added). I fail to see how anyone can think that saying a statute does not impose an
        unconstitutional burden under <i>any</i> standard, including the undue burden test, amounts to adopting the
        undue burden test as the <i>exclusive</i> standard. The Court's citation of <i>Hodgson</i> as reflecting Justice
        Kennedy's and Justice O'Connor's \"shared premises,\" <i>ante,</i> at 878, is similarly inexplicable, since the
        word \"undue\" was never even used in the former's opinion in that case.I joined Justice Kennedy's opinions in
        both <i>Hodgson</i> and <i>Akron II;</i> I should be grateful, I suppose, that the joint opinion does not claim
        that I, too, have adopted the undue burden test.
    </p>\n<p>[5] Of course Justice O'Connor was correct in her
        former view. The arbitrariness of the viability line is confirmed by the Court's inability to offer any
        justification for it beyond the conclusory assertion that it is only at that point that the unborn child's life
        \"can in reason and all fairness\" be thought to override the interests of the mother. <i>Ante,</i> at 870.
        Precisely why is it that, at the magical second when machines currently in use (though not necessarily available
        to the particular woman) are able to keep an unborn child alive apart from its mother, the creature is suddenly
        able (under our Constitution) to be protected by law, whereas before that magical second it was not? That makes
        no more sense than according infants legal protection only after the point when they can feed themselves.</p>\n
    <p>[6] The joint opinion is not entirely faithful to this principle, however. In approving the District Court's
        factual findings with respect to the spousal notice provision, it relies extensively on nonrecord materials, and
        in reliance upon them adds a number of factual conclusions of its own. <i>Ante,</i> at 891-893. Because this
        additional factfinding pertains to matters that surely are \"subject to reasonable dispute,\" Fed. Rule Evid.
        201(b), the joint opinion must be operating on the premise that these are \"legislative\" rather than
        \"adjudicative\" facts, see Rule 201(a). But if a court can find an undue burden simply by selectively
        string-citing the right social science articles, I do not see the point of emphasizing or requiring \"detailed
        factual findings\" in the District Court.</p>\n<p>[7] Justice Blackmun's effort to preserve as much of
        <i>Roe</i> as possible leads him to read the joint opinion as more \"constan[t]\" and \"steadfast\" than can be
        believed. He contends that the joint opinion's \"undue burden\" standard requires the application of strict
        scrutiny to \"all non-<i>de-minimis</i> \" abortion regulations, <i>ante,</i> at 926, but that could only be
        true if a \"substantial obstacle,\" <i>ante,</i> at 877 (joint opinion), were the same thing as a
        non<i>de-minimis</i> obstaclewhich it plainly is not.
    </p>\n\n
</div>"""
        }
    ],
)

print(response.choices[0].message.content)