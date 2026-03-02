---
title: "Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding"
collection: publications
category: manuscripts
permalink: /publication/2025-12-05-zoomclick
excerpt: 'A training-free method that leverages zooming as a powerful prior for GUI grounding, achieving state-of-the-art results across multiple benchmarks.'
date: 2025-12-05
venue: 'arXiv preprint'
paperurl: 'https://arxiv.org/abs/2512.05941'
citation: 'Jiang, Z., Xie, S., Li, W., Zu, W., Li, P., Qiu, J., Pei, S., Ma, L., Huang, T., Wang, M., & Liu, S. (2025). &quot;Zoom in, Click out: Unlocking and Evaluating the Potential of Zooming for GUI Grounding.&quot; <i>arXiv preprint arXiv:2512.05941</i>.'
---

<img src="/images/zoomclick.png" alt="ZoomClick Method Overview" style="width:100%; margin-bottom:20px;">

## Overview

GUI grounding—the ability to locate UI elements from natural language—is fundamental for building autonomous GUI agents. Existing approaches rely on large-scale bounding box supervision but still struggle with cross-platform generalization, complex layouts, and fine-grained localization.

## Key Contributions

- **Zoom as a Prior**: We discover that zooming provides a powerful yet underexplored prior for GUI grounding, enabling dynamic spatial focusing and adaptive context switching.

- **Training-Free Method**: ZoomClick requires no additional training and works with both general VLMs and specialized GUI grounding models.

- **Four Key Properties**: We characterize pre-zoom, depth, shrink size, and minimal crop size to unlock zoom's full potential.

- **State-of-the-Art Results**: UI-Venus-72B achieves 73.1% success rate on ScreenSpot-Pro; smaller models match larger ones' performance.

- **GUIZoom-Bench**: A new benchmark for evaluating model adaptability to zoom, enabling future research on test-time scaling.

[arXiv](https://arxiv.org/abs/2512.05941) | [Code](https://github.com/Princeton-AI2-Lab/ZoomClick)
