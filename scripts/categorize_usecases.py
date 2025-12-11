#!/usr/bin/env python3
"""Categorize use cases and generate updated index with category tables."""

import re
from pathlib import Path

# Categories from category.md
CATEGORIES = {
    "Work – Multi-Client / Multi-Project": [
        (1, "Consultant With Three Clients and No Time", "Independent consultant / fractional PM", "consultant.md"),
        (2, "Neurodivergent Builder With 5 Parallel Projects", "Neurodivergent builder / product-minded founder", "neurodivergent-builder.md"),
        (3, "Sales Rep Chasing a Whale Account", "Sales rep / account executive", None),
        (11, "Product Manager With Three Streams and a 15-Minute Gap", "Product manager (often ND, many streams)", "product-manager.md"),
        (12, "Sales Engineer Prepping Two Completely Different Demos", "Sales engineer / solutions architect", None),
        (13, "Customer Success Manager Surfacing From One Renewal Into Another", "Customer success manager", None),
        (21, "Small Agency Founder With Three Clients Pulling at Once", "Agency founder / creative director", None),
        (22, "Solo Developer/Indie Hacker Pinballing Between Code, Bugs, and Launch", "Solo developer / indie hacker", None),
        (27, "Wedding Photographer Moving From Planning to Shooting to Editing", "Wedding photographer / creative freelancer", None),
        (33, "Film Editor Cutting a Feature and a Trailer for a Different Client", "Film editor / post-production", None),
        (44, "Financial Planner Running Three Client Reviews in One Morning", "Financial planner / wealth advisor", None),
    ],
    "Work – Ops, Incidents & Live Operations": [
        (8, "DevOps Responding to a Production Incident", "DevOps engineer / SRE", "devops.md"),
        (9, "Emergency Manager Handling a Gas Leak With Multiple Agencies", "Emergency manager / incident commander", None),
        (16, "DevOps Engineer Moving From Postmortem to Reliability Review", "DevOps engineer / SRE", None),
        (17, "Emergency Manager Switching From 'Gas Leak' to 'Storm Prep'", "Emergency manager / EOC coordinator", None),
        (32, "Manufacturing Ops Manager Between Factory Floor, Supplier Crisis, and Audit", "Manufacturing ops manager", None),
        (35, "Festival Ops Lead Juggling Security, Weather, and Artist Schedules", "Festival ops lead / event manager", None),
        (41, "Emergency Vet Switching From One Crisis to the Next", "Emergency veterinarian", None),
        (42, "Airline Operations Controller in a Storm", "Airline operations controller", None),
        (43, "Construction Site Foreman Between Subcontractors, Deliveries, and Safety", "Construction foreman / site manager", None),
    ],
    "Work – Rituals, Meetings & Team Rhythms": [
        (4, "Scrum Master With a Standup That Can Run Without Them", "Scrum master / agile coach", "scrum-master.md"),
        (7, "Corporate Manager Living in 12 SaaS Tools All Day", "Corporate manager / team lead", None),
        (18, "Corporate Manager With Back-to-Back 'Different Universe' Meetings", "Corporate manager / director", None),
        (25, "Teacher Running Back-to-Back Classes and Then a Parent Meeting", "Teacher / educator", None),
        (26, "Conference Organizer Switching Between Sponsors, Speakers, and Venue", "Conference organizer / event planner", None),
        (30, "Recruiter Running a Full Interview Loop for One Candidate", "Recruiter / talent acquisition", None),
        (36, "HR Generalist Dealing With a Grievance, an Offer, and a Policy Rollout", "HR generalist / people ops", None),
        (48, "University Lecturer Split Between Teaching, Research, and Admin", "University lecturer / academic", None),
    ],
    "Work – Deep Work, Research & Analysis": [
        (14, "Data Analyst With Three Urgent Requests From Different Execs", "Data analyst / BI specialist", None),
        (15, "Startup Founder Doing Board Prep Between Fires", "Startup founder / CEO", None),
        (19, "UX Researcher Jumping Between Live Sessions and Synthesis", "UX researcher", None),
        (20, "Marketing Lead Orchestrating a Launch Across Channels", "Marketing lead / growth manager", None),
        (37, "Investment Analyst Covering Three Sectors on Earnings Week", "Investment analyst / equity researcher", None),
        (38, "City Planner Balancing a New Transport Corridor, a Housing Project, and Public Input", "City planner / urban designer", None),
        (39, "Policy Lobbyist Prepping Lawmakers for a Committee Hearing", "Policy lobbyist / government affairs", None),
        (47, "Penetration Tester Handling Two Engagements Plus Reporting", "Penetration tester / security consultant", None),
    ],
    "Work – SME & Multi-Role Founders": [
        (6, "SME Owner Running the Business From 6 Different Apps", "SME owner / studio founder", "sme-owner.md"),
        (23, "Real Estate Agent on the Road Between Buyers and Sellers", "Real estate agent / broker", None),
        (28, "YouTuber / Streamer Jumping Between Prep, Live, and Post", "YouTuber / content creator / streamer", None),
        (29, "NGO Program Manager Between Field Updates and Donor Reports", "NGO program manager", None),
        (40, "Remote-First Founder Doing Investor Pitch, Hiring Interview, and Roadmap Review", "Remote-first founder / CEO", "remote-founder.md"),
        (46, "Veterinary Clinic Owner Balancing Patients, Staff, and Business", "Veterinary clinic owner", None),
        (59, "Artist Turning a Hobby Into a Small Online Shop", "Artist / creative entrepreneur", None),
    ],
    "Work – Legal & Crisis": [
        (31, "Public Defender in LA, 100 Degrees, Court in 10 Minutes", "Public defender (criminal defence)", "public-defender.md"),
        (24, "Doctor in Clinic Moving From Routine Checkups to a Scary Lab Result", "Doctor / GP / clinician", None),
        (34, "Hospital Social Worker Handling Three Complex Discharges", "Hospital social worker", None),
    ],
    "Life – Admin, Money & Systems": [
        (10, "Personal Finances & Taxes – With an Accountant in the Loop", "Anyone doing tax prep / personal finances", None),
        (58, "Person Planning a Big Move to Another Country", "Person relocating internationally", None),
        (67, "Executor Handling Estate and Paperwork After a Death", "Estate executor / administrator", None),
    ],
    "Life – Health, Recovery & Performance": [
        (52, "Bill, 240lbs, Training for His First Marathon", "First-time marathoner / fitness beginner", "marathon-training.md"),
        (56, "Recently Sober Person Balancing Recovery, Work, and Rebuilding Life", "Person in recovery", None),
        (65, "Preparing for Surgery in 4 Weeks", "Patient facing surgery", "surgery-prep.md"),
    ],
    "Life – Family, Care & School": [
        (5, "ND Parent With School Chaos and Shared Mental Load", "Parent of school-age child (often ND)", "nd-parent.md"),
        (51, "Mum With a Son Who Has Special Needs – The Call From the School", "Parent of child with special needs", "special-needs-mum.md"),
        (50, "Parent Planning a Multi-Country Trip With Their Partner", "Parent planning family travel", None),
        (55, "Caregiver for an Ageing Parent", "Adult child caring for ageing parent", "caregiver.md"),
    ],
    "Life – Crisis, Loss & Legal Aftermath": [
        (66, "Funeral Planning While Grieving", "Adult child planning a parent's funeral", "funeral-planning.md"),
        (53, "Anne, Laid Off, on a Weekly Accountability Call With Three Also-Fired Friends", "Laid-off professional in job search", None),
    ],
    "Life – Dreams, Second Act & Identity": [
        (61, "Retiree Starting a Second Act Instead of Just Drifting", "Retired professional starting chapter 2", "retiree.md"),
        (68, "Midlife 'Quiet Crisis' – Life's Okay, But They Know It's Not Fine", "Midlife professional reassessing", None),
        (69, "Professor Running for State Senator Under Fire", "Academic entering politics", None),
        (70, "Ger: Feeding His Family From the Back Garden in Two Years", "Homeowner seeking food independence", None),
        (71, "Mary, Who Acted 20 Years Ago and Buried It", "Former creative returning to first love", "returning-actor.md"),
        (72, "Climate-Anxious Engineer Building a Local Resilience Project", "Climate-conscious professional", None),
        (73, "Nurse on Night Shifts, Secretly Writing a Novel", "Professional with hidden creative ambition", None),
    ],
    "Life – Learning, Education & Future Self": [
        (54, "Anne Building an App, One Customer at a Time", "Career-changer learning to build", None),
        (57, "Community Organizer Leading a Tenant Group", "Community organizer / activist", None),
        (60, "Young Adult Balancing Uni, Side Hustle, and Family Expectations", "University student with side projects", None),
        (62, "Youth Trying to Get Into College – Applications, Essays, Panic", "High school senior applying to college", None),
        (63, "Failing Student Overwhelmed and Quietly Drowning", "Struggling student", None),
        (64, "The Procrastinator Who Keeps Saying 'It's Fine' While Ignoring Alarms", "Chronic procrastinator", None),
        (45, "Dungeon Master Running Multiple Campaigns", "Dungeon master / TTRPG game master", None),
        (49, "Genealogy Hobbyist Piecing Together a Family Line", "Genealogy researcher / family historian", None),
    ],
}


def slugify(title: str) -> str:
    """Convert title to anchor slug."""
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    return slug


def generate_category_tables() -> str:
    """Generate markdown tables organized by category."""
    output = []

    for category, use_cases in CATEGORIES.items():
        output.append(f"### {category}\n")
        output.append("| # | Who am I? | Scenario | Read |")
        output.append("|---|-----------|----------|------|")

        for num, title, persona, dedicated_page in sorted(use_cases, key=lambda x: x[0]):
            if dedicated_page:
                link = f"[Read →]({dedicated_page})"
            else:
                slug = slugify(f"{num}-{title}")
                link = f"[Read](#{slug})"

            output.append(f"| {num} | {persona} | {title} | {link} |")

        output.append("")

    return "\n".join(output)


def generate_hero_table() -> str:
    """Generate the hero use cases table with all columns from category.md."""
    heroes = [
        ("Work – Multi-Client / Multi-Project", "Independent consultant / fractional PM", "Three clients, back-to-back calls, no time to breathe", "`Client – [Name] – Project`", "One-click 'world per client' for instant context re-entry", "consultant.md"),
        ("Work – Multi-Client / Multi-Project", "Neurodivergent builder / founder", "5 parallel projects, ADHD brain, hyperfocus bursts", "`Project – [Name]`", "Save & reload 'brain states' per project", "neurodivergent-builder.md"),
        ("Work – Rituals & Team Rhythms", "Scrum master / agile coach", "Daily standup + planning + being out sick", "`Scrum – Standup Stax`", "A standup cockpit anyone on the team can run", "scrum-master.md"),
        ("Work – SME & Multi-Role", "SME owner / studio founder", "Running the business from 6 different apps", "`Biz – Daily Ops`", "Turns tool soup into a single daily control room", "sme-owner.md"),
        ("Work – Ops & Incidents", "DevOps engineer / SRE", "P1 incident just triggered", "`P1 – [Symptom / Service]`", "Shared incident war room in one Stax", "devops.md"),
        ("Work – Multi-Client / Multi-Project", "Product manager (often ND)", "Three streams, 15-minute gaps between meetings", "`PM – [Stream Name]`", "Clean mental switch between streams in seconds", "product-manager.md"),
        ("Work – Legal & Crisis", "Public defender", "100°F in LA, court in 10 minutes, multiple cases", "`Case – [Client Name]`", "Walk into court coherent, not scrambling", "public-defender.md"),
        ("Work – SME & Multi-Role", "Remote-first founder", "Investor pitch, hiring interview, roadmap review", "`Founder – [Context]`", "Separate 'rooms' so you show up present", "remote-founder.md"),
        ("Life – Family & School", "Parent of ND child", "School calls about incident; meeting tomorrow", "`[Child] – School & Supports`", "All portals and agreements in one shared Stax", "nd-parent.md"),
        ("Life – Family & School", "Parent of child with special needs", "The call from school, IEP meetings", "`[Child] – Special Needs`", "Shared cockpit with co-parent and specialists", "special-needs-mum.md"),
        ("Life – Health & Recovery", "Patient facing surgery", "Operation in 4 weeks; work, home, hospital logistics", "`Surgery – Operation & Recovery`", "Timeline-based plan shared with family", "surgery-prep.md"),
        ("Life – Crisis & Loss", "Adult child planning funeral", "Organising funeral while grieving", "`Funeral – [Name] – Farewell`", "Admin scaffolding when brain is overloaded", "funeral-planning.md"),
        ("Life – Dreams & Second Act", "Retired professional", "Sorting pensions & designing meaningful chapter 2", "`Retirement – Second Act`", "Turn vague 'someday' into concrete experiment", "retiree.md"),
        ("Life – Health & Recovery", "240lb first-time marathoner", "16-20 week build, wants to finish healthy", "`Bill – Marathon 2025`", "Plan, progress, realistic non-heroic steps", "marathon-training.md"),
        ("Life – Dreams & Second Act", "Former actor / creative", "20 years later, trying again before it's too late", "`Mary – Return to Acting`", "Safe, structured way to attempt the dream", "returning-actor.md"),
        ("Life – Family & Care", "Caregiver for ageing parent", "Medical, legal, benefits, siblings all at once", "`Mum/Dad – Health & Life Admin`", "One shared cockpit for the responsible child", "caregiver.md"),
    ]

    output = ["### Hero Use Cases\n"]
    output.append("| Category | Who am I? | Scenario | Stax Pattern | What It Gives You | Read |")
    output.append("|----------|-----------|----------|--------------|-------------------|------|")

    for cat, persona, scenario, pattern, benefit, page in heroes:
        output.append(f"| {cat} | {persona} | {scenario} | {pattern} | {benefit} | [Read →]({page}) |")

    output.append("")
    return "\n".join(output)


def extract_stories_from_index(index_path: Path) -> str:
    """Extract the full stories section from existing index.md."""
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where "## Full Stories" or "## 3. Sales Rep" starts (first inline story)
    match = re.search(r'^## Full Stories\n', content, re.MULTILINE)
    if match:
        return content[match.start():]

    # Fallback: find first ## with a number (inline story)
    match = re.search(r'^## \d+\.', content, re.MULTILINE)
    if match:
        return "## Full Stories\n\nThe stories below use the original content from our use case collection. For the Core Heroes, click their links above to read their dedicated pages.\n\n---\n\n" + content[match.start():]

    return ""


def main():
    usecases_dir = Path(__file__).parent.parent / 'topics' / 'usecases'
    index_path = usecases_dir / 'index.md'
    output_file = usecases_dir / 'index.md'

    # Extract existing stories
    stories_content = extract_stories_from_index(index_path)

    content = """[← Back to Help Home](../../README.md)

# Using TabStax in Your Job and Your Life

**Real people. Real chaos. Real Stax.**

Below you'll find over 70 ways people actually use TabStax—from high-pressure work scenarios to deeply personal life moments. Each story shows how a named workspace with tabs, next actions, and context can cut through chaos and help you stay present.

---

## Quick Navigation

- [Hero Use Cases](#hero-use-cases) – 16 detailed stories with dedicated pages
- [Work Use Cases](#work-use-cases) – Professional scenarios by category
- [Life Use Cases](#life-use-cases) – Personal and life admin scenarios

---

"""

    # Add hero table
    content += generate_hero_table()
    content += "\n---\n\n"

    # Add Work categories
    content += "## Work Use Cases\n\n"
    work_categories = [k for k in CATEGORIES.keys() if k.startswith("Work")]
    for cat in work_categories:
        use_cases = CATEGORIES[cat]
        content += f"### {cat}\n\n"
        content += "| # | Who am I? | Scenario | Read |\n"
        content += "|---|-----------|----------|------|\n"
        for num, title, persona, page in sorted(use_cases, key=lambda x: x[0]):
            if page:
                link = f"[Read →]({page})"
            else:
                slug = slugify(f"{num}-{title}")
                link = f"[Read](#{slug})"
            content += f"| {num} | {persona} | {title} | {link} |\n"
        content += "\n"

    content += "---\n\n"

    # Add Life categories
    content += "## Life Use Cases\n\n"
    life_categories = [k for k in CATEGORIES.keys() if k.startswith("Life")]
    for cat in life_categories:
        use_cases = CATEGORIES[cat]
        content += f"### {cat}\n\n"
        content += "| # | Who am I? | Scenario | Read |\n"
        content += "|---|-----------|----------|------|\n"
        for num, title, persona, page in sorted(use_cases, key=lambda x: x[0]):
            if page:
                link = f"[Read →]({page})"
            else:
                slug = slugify(f"{num}-{title}")
                link = f"[Read](#{slug})"
            content += f"| {num} | {persona} | {title} | {link} |\n"
        content += "\n"

    # Append the full stories section
    content += "\n---\n\n"
    content += stories_content

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated index with categorized tables at {output_file}")


if __name__ == '__main__':
    main()
