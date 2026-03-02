---
title: "Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding"
collection: publications
category: manuscripts
permalink: /publication/2025-12-05-zoomclick
excerpt: 'We investigate zoom as a strong yet underexplored prior for GUI grounding, and propose a training-free method, ZoomClick, achieving state-of-the-art results.'
date: 2025-12-05
venue: 'arXiv preprint'
paperurl: 'https://arxiv.org/abs/2512.05941'
citation: 'Jiang, Z., Xie, S., Li, W., Zu, W., Li, P., Qiu, J., Pei, S., Ma, L., Huang, T., Wang, M., & Liu, S. (2025). Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding. arXiv preprint arXiv:2512.05941.'
---

Grounding is a fundamental capability for building graphical user interface (GUI) agents. Although existing approaches rely on large-scale bounding box supervision, they still face various challenges, such as cross-platform generalization, complex layout analysis, and fine-grained element localization. 

In this paper, we investigate zoom as a strong yet underexplored prior for GUI grounding, and propose a training-free method, ZoomClick. By characterizing four key properties of zoom (i.e., pre-zoom, depth, shrink size, minimal crop size), we unlock its full capabilities for dynamic spatial focusing and adaptive context switching. 

Experiments demonstrate that our method significantly boosts the performance of both general vision-language and specialized GUI grounding models, achieving state-of-the-art results on several mainstream benchmarks; for example, UI-Venus-72B attains a 73.1% success rate on ScreenSpot-Pro.

[arXiv](https://arxiv.org/abs/2512.05941) | [Code](https://github.com/Princeton-AI2-Lab/ZoomClick)
