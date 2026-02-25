# Launch Day Checklist

## Pre-Launch (Night Before)

- [ ] Verify all 611 skills have valid SKILL.md with correct YAML frontmatter
- [ ] Confirm README.md is polished with clear description, structure, and contributing guide
- [ ] Ensure LICENSE file (MIT) is present in repo root
- [ ] Verify CONTRIBUTING.md exists with clear skill authoring instructions
- [ ] Check that repo description and topics are set on GitHub (cybersecurity, ai, agents, security, open-source)
- [ ] Pin the most impressive/representative issues (good first issues, feature requests)
- [ ] Confirm GitHub Actions CI passes on main branch
- [ ] Pre-write all launch posts (HN, Reddit, Twitter, LinkedIn, Dev.to) and have them ready to paste
- [ ] Test all links in launch posts point to correct repo URLs
- [ ] Draft responses to anticipated questions (see FAQ prep below)
- [ ] Set up monitoring: GitHub notifications on, email alerts for new issues/stars
- [ ] Ensure the repo is public (not private or internal)

## Launch Morning

### Hour 0: Go Live

- [ ] **6:00 AM Pacific / 9:00 AM Eastern**: Post Show HN on Hacker News
  - Title: "Show HN: 611+ Cybersecurity Skills for AI Agents (agentskills.io open standard)"
  - Paste body from `launch/hacker-news.md`
- [ ] Immediately after HN: Post first Reddit post to r/netsec
- [ ] Post Twitter/X thread (all 7 tweets)
- [ ] Post LinkedIn article
- [ ] Bookmark HN post URL for monitoring

### Hour 1-2: First Engagement Wave

- [ ] Monitor HN for comments -- respond to every comment within 1 hour
- [ ] Be technical in HN responses: reference specific skill files, tool commands, MITRE technique IDs
- [ ] Do NOT ask for upvotes anywhere -- ever
- [ ] Post to r/cybersecurity (2 hours after r/netsec post)

### Hour 3-4: Second Wave

- [ ] Post to r/blueteamsec
- [ ] Post to r/hacking
- [ ] Continue monitoring and responding to HN and Reddit comments
- [ ] Track GitHub stars, forks, and issues

### Hour 5-6: Third Wave

- [ ] Post to r/redteamsec
- [ ] Post to r/artificial
- [ ] Post to r/opensource
- [ ] Publish Dev.to article

### Throughout the Day

- [ ] Respond to every GitHub issue within 2 hours
- [ ] Respond to every Reddit comment with substance
- [ ] Thank anyone who stars or shares the repo
- [ ] If any post gains traction, share it on Twitter with a brief note
- [ ] Monitor for any negative feedback or valid criticisms -- address them transparently

## End of Day 1

- [ ] Record metrics: GitHub stars, forks, issues, traffic (Insights tab)
- [ ] Record metrics: HN points and rank position, Reddit upvotes per post
- [ ] Identify top questions/concerns from community -- plan content to address them
- [ ] Merge any quick-win PRs that come in (shows the project is active and welcoming)
- [ ] Post a "Day 1" update on Twitter if there's traction: "Thank you for the response. X stars, Y issues filed, here's what we're working on next."
- [ ] Join Discord servers (see `launch/discord-servers.md`) and introduce yourself and the project

## Day 2+

- [ ] Send press email to Help Net Security (see `launch/help-net-security-email.md`)
- [ ] Continue engaging with all platforms daily for at least 1 week
- [ ] Post in Discord servers where appropriate (don't spam -- contribute value first, then mention the project)
- [ ] Write follow-up content based on community feedback:
  - Blog post addressing top questions
  - Tutorial: "How to contribute a skill in 10 minutes"
  - Deep dive into a specific subdomain
- [ ] Reach out to security influencers who engaged with the launch posts
- [ ] Track weekly metrics: stars, forks, contributors, issues opened/closed
- [ ] Plan the first community call or AMA if there's sufficient interest
- [ ] Submit to security newsletters (tl;dr sec, SANS NewsBites, etc.)
- [ ] Look for podcast/webinar opportunities if the project gets 500+ stars

## FAQ Prep (Anticipated Questions)

**"Aren't these just runbooks/cheat sheets?"**
> They're structured for machine consumption, not just human reading. The YAML frontmatter provides routing metadata that lets an agent know WHEN to use a skill, and the body provides the exact HOW. A cheat sheet doesn't have activation conditions or progressive disclosure.

**"Can AI actually do security work?"**
> Not autonomously, and that's not the goal. These skills make AI agents useful assistants -- like giving a junior analyst a detailed procedure library. The human makes decisions; the agent provides precise, tool-specific guidance.

**"Why not just fine-tune a model?"**
> Fine-tuning is expensive, hard to audit, and requires retraining for every update. A skill file can be reviewed, version-controlled, and updated by any practitioner. It's also transparent -- you can read exactly what the agent will do.

**"Is this just for Claude/Anthropic?"**
> No. The agentskills.io format is agent-agnostic. Any AI agent that can read files can use these skills. The format is intentionally simple (YAML + Markdown) for maximum compatibility.

**"How do you ensure quality?"**
> Every skill references real tools with real commands. Contributors are expected to be practitioners. The community review process catches errors. Bad skills get issues filed against them.
