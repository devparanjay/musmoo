<!-- Project Title -->
<h1 align="center">MusMoo</h1>

<!-- Project Description -->
<p align="center">A Python application that detects user emotions via AI and recommends personalized songs based on emotional state.</p>

<!-- Badges -->
<p align="center">
  <a href="https://github.com/devparanjay/musmoo/tree/alpha"><img alt="Stage Alpha" src="https://img.shields.io/badge/stage-alpha-cyan"></a>
  <a href="#"><img src="https://img.shields.io/badge/version-0.0.2-brightgreen" alt="Version 0.0.2"></a>
  <a href="https://github.com/devparanjay/musmoo/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-AGPL_3.0-blue" alt="License: AGPL 3.0"></a>
</p>

<!-- Overview -->
## Overview
When launched, MusMoo engages users with thoughtful questions to gauge their emotional state. Leveraging an advanced emotion detection model, it then curates mood-based music recommendations and fetches them using the 'ytmusicapi' library. The suggestions are saved in TXT files within the /recommendations folder, ready to be used for creating YouTube Music playlists.

## Features
- Personalized emotional state detection
- Mood-based song recommendations
- Songs output in .txt with one song URL per line

## Getting Started
To use MusMoo, follow these simple steps:
1. Clone the repository to your local machine.
2. Install dependencies using `pip install -r requirements.txt` OR `pip install -r requirements-gpu.txt` (recommended if you have a GPU).
3. Run the application and answer the prompted questions to receive personalized music recommendations.

## Future Roadmap
As MusMoo progresses through development, the following enhancements are planned:
- Fine-tuning recommendation engine for enhanced accuracy
- Better and less questions for emotion detection
- Direct playlist creation from the application
- Robust error handling for improved user experience
- Implementation of an intuitive graphical user interface (GUI)

<!-- Authors -->
## Authors
- [@devparanjay](https://github.com/devparanjay)

<!-- Citations -->
## Citations
- Hsu, Lun-Kai & Tseng, Wen-Sheng & Kang, Li-Wei & Wang, Yu-Chiang Frank. (2013). Seeing through the expression: Bridging the gap between expression and emotion recognition. Proceedings - IEEE International Conference on Multimedia and Expo. 1-6. 10.1109/ICME.2013.6607638.
<br>https://www.researchgate.net/publication/261160494_Seeing_through_the_expression_Bridging_the_gap_between_expression_and_emotion_recognition
- Hepach, R., Kliemann, D., Grüneisen, S., Heekeren, H. R., & Dziobek, I. (2011). Conceptualizing emotions along the dimensions of valence, arousal, and communicative frequency - implications for social-cognitive tests and training tools. Frontiers in psychology, 2, 266.
<br>https://doi.org/10.3389/fpsyg.2011.00266, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3196197/

<!-- Acknowledgments -->
## Acknowledgments
- [ytmusicapi](https://github.com/sigma67/ytmusicapi)
- [Sam Lowe](https://github.com/samlowe)

<!-- Licence -->
## License
This project is licensed under the [Aferro GPL 3.0] License - see the [LICENSE](https://github.com/devparanjay/musmoo/blob/main/LICENSE) file for more details.
In short, any usage and derivation of this application and its code comes with the following limitations -
- License and copyright notice
- State changes
- Disclose source
- Network use is distribution
- Same license

<!-- End of README -->
