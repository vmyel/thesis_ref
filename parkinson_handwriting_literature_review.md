# Literature Review: Machine Learning Models for Handwriting and Drawing-Based Severity Assessment in Parkinson's Disease

## Top 5 Articles for Thesis: "From Pen Strokes to Prognosis: Machine Learning Models for Handwriting and Drawing-Based Severity Assessment in Parkinson's Disease"

---

### 1. Deep Learning Analysis of Figure Copying Tasks for Parkinson's Disease Detection

**APA Citation:**
Vallejo, M., Alty, J., & Smith, S. L. (2025). Deep learning analysis of figure copying tasks for Parkinson's disease detection with GAN-based data augmentation. *medRxiv*. https://doi.org/10.1101/2025.04.15.25325847

**Summary (80-100 words):**
This study investigated whether convolutional neural networks (CNNs) could automate Parkinson's disease detection through figure copying tasks. Research question focused on optimizing deep learning models for PD screening using digital pen data. Eighty-two drawings from 56 PD patients and 26 controls were analyzed across three visual modalities: time, pressure, and pen angle. To address limited dataset size, researchers employed data augmentation techniques including generative adversarial networks (GANs). Findings showed highest classification accuracy of 80.14% using pen pressure representations with traditional augmentation methods, demonstrating CNN potential for non-invasive PD screening.

**Relevance to Proposal (150-200 words):**
This research directly supports your thesis foundation by demonstrating the effectiveness of deep learning models, particularly CNNs, in analyzing drawing tasks for Parkinson's disease detection. The study's emphasis on pen pressure as a discriminative feature aligns perfectly with your focus on handwriting-based severity assessment, suggesting that pressure dynamics could be a crucial biomarker in your proposed models. The exploration of data augmentation techniques, especially GANs, provides valuable methodological insights for handling limited datasets—a common challenge in medical machine learning research that you will likely encounter. The study introduces key concepts of multimodal data analysis (time, pressure, pen angle) that could form the foundation of your feature extraction approach. Additionally, the research addresses shortcomings in prior work by tackling the small dataset problem through sophisticated augmentation strategies, offering methods you can adapt. The 80.14% accuracy benchmark provides a performance baseline for comparison with your models, while the focus on non-invasive screening tools aligns with the clinical applicability goals of your research.

---

### 2. Automatic Diagnosis of Parkinson's Disease Using Handwriting Patterns

**APA Citation:**
Nagamani, T., Jayadeep, K. J. V. S., Sandhya, J., Lahari, K. S. S., & Babu, G. P. (2024). Automatic diagnosis of Parkinson's disease using handwriting patterns. *Journal of Electrical Systems*, *20*(7s). https://journal.esrgroups.org/jes/article/view/3712

**Summary (80-100 words):**
This research explored computer vision and machine learning techniques for PD detection using spiral and wave handwriting patterns. The study addressed how effectively Histogram of Oriented Gradients (HOG) features could distinguish PD patients from healthy controls. Researchers analyzed frontal handwritten images standardized to 200x200 pixels from Spiral-Wave tests. HOG was employed for feature extraction, followed by Random Forest and K-Nearest Neighbors (KNN) classification. Findings demonstrated accuracies of 86.67% for spiral images and 76.67% for wave images, with Random Forest outperforming KNN. Results confirmed the effectiveness of combining HOG features with machine learning classifiers for precise PD analysis.

**Relevance to Proposal (150-200 words):**
This study provides crucial methodological insights for your thesis by demonstrating the application of computer vision techniques to handwriting pattern analysis in Parkinson's disease detection. The research introduces HOG as a key feature extraction method that could be integrated into your severity assessment models, particularly for analyzing spiral and wave drawing patterns—standard clinical tests for PD motor symptoms. The comparative analysis of Random Forest and KNN classifiers offers valuable guidance for your classifier selection process, with Random Forest showing superior performance that could inform your model architecture decisions. The study addresses the concept of pattern recognition in handwriting, which is fundamental to your work's foundation. The reported accuracies (86.67% and 76.67%) establish performance benchmarks and highlight the discriminative power of geometric features in handwriting analysis. This research also demonstrates methods for standardizing handwriting images, which will be essential for preprocessing in your proposed pipeline. The focus on spiral and wave patterns specifically relates to clinical assessment tools used in PD diagnosis, ensuring your work maintains clinical relevance and practical applicability.

---

### 3. Sequence-Based Dynamic Handwriting Analysis for Parkinson's Disease Detection

**APA Citation:**
Díaz, M., Moetesum, M., Siddiqi, I., & Vessio, G. (2021). Sequence-based dynamic handwriting analysis for Parkinson's disease detection with one-dimensional convolutions and BiGRUs. *arXiv preprint arXiv:2101.09461*. https://arxiv.org/abs/2101.09461

**Summary (80-100 words):**
This study investigated whether sequential handwriting information could improve PD detection using hybrid neural networks. Research questions focused on capturing spatio-temporal properties in handwriting dynamics for identifying Parkinsonian symptoms. The proposed model combined one-dimensional convolutions with Bidirectional Gated Recurrent Units (BiGRUs) to process raw sequences and derived features. Evaluation on PaHaW and NewHandPD datasets showed state-of-the-art performance on PaHaW and competitive results on NewHandPD. Key findings demonstrated that sequential patterns in handwriting effectively distinguish PD patients from healthy individuals, with the hybrid architecture capturing both spatial and temporal dynamics crucial for accurate classification.

**Relevance to Proposal (150-200 words):**
This research is particularly valuable for your thesis as it introduces a sophisticated framework for analyzing the sequential nature of handwriting data, which is central to understanding motor dysfunction in Parkinson's disease. The combination of convolutional and recurrent neural networks offers a robust methodological approach that you can adapt for severity assessment, moving beyond simple classification to potentially quantify disease progression. The study's emphasis on capturing spatio-temporal properties addresses a key concept in your work—that handwriting dynamics contain rich temporal information reflecting motor control deterioration. The research demonstrates methods for processing both raw sequences and derived features, providing multiple pathways for feature engineering in your models. The validation on established datasets (PaHaW and NewHandPD) offers benchmark comparisons and suggests these datasets could be valuable for your research. The study addresses shortcomings in prior work that focused primarily on static features, introducing the importance of temporal dynamics. The hybrid architecture's success points to advanced neural network techniques that could enhance your severity assessment models beyond traditional machine learning approaches, potentially enabling more nuanced gradations of disease severity.

---

### 4. Cross-Corpus and Cross-Domain Handwriting Assessment via Time-Series-to-Image Conversion

**APA Citation:**
Chavez, G., Moro-Velazquez, L., Butala, A., Dehak, N., & Thebaud, T. (2025). Cross-corpus and cross-domain handwriting assessment of neurodegenerative diseases via time-series-to-image conversion. *arXiv preprint arXiv:2509.16474*. https://arxiv.org/abs/2509.16474

**Summary (80-100 words):**
This research examined whether converting time-series handwriting data into image representations could improve neurodegenerative disease detection across multiple datasets. The study investigated cross-corpus and cross-domain generalization using a ResNet50 model pretrained on ImageNet-1k. Researchers analyzed handwriting signals from various datasets including the NeuroLogical Signals (NLS) dataset. The innovative time-series-to-image conversion framework achieved state-of-the-art performance with F1 scores up to 98 in PD detection tasks. Findings demonstrated significant improvements in drawing and writing tasks, highlighting the potential of integrating different forms of handwriting signals for enhanced motor deficit detection.

**Relevance to Proposal (150-200 words):**
This study introduces a groundbreaking approach highly relevant to your thesis by demonstrating innovative data representation techniques that could significantly enhance your severity assessment models. The time-series-to-image conversion method presents a novel way to leverage the power of pretrained computer vision models for handwriting analysis, potentially improving feature extraction and model performance in your work. The research addresses a critical challenge in machine learning for medical applications—model generalization across different datasets and domains—which is essential for developing clinically viable severity assessment tools. The cross-corpus validation approach provides methods you can use to ensure your models work effectively across diverse patient populations and data collection protocols. The study explains advanced techniques for handling temporal handwriting data that could be foundational to your methodology, particularly for capturing the dynamic aspects of motor deterioration in PD. The exceptional performance (F1 scores up to 98) demonstrates the potential of this approach and sets high benchmarks for your work. This research also points out limitations in traditional time-series analysis approaches, offering you a method to address these shortcomings through innovative data transformation techniques.

---

### 5. Machine Learning for Real-Time Automatic Diagnosis of Parkinson's Disease

**APA Citation:**
Tyagi, R., Tyagi, T., Wang, M., & Zhang, L. (2021). Machine learning for real-time, automatic, and early diagnosis of Parkinson's disease by extracting signs of micrographia from handwriting images. *arXiv preprint arXiv:2111.14781*. https://arxiv.org/abs/2111.14781

**Summary (80-100 words):**
This study investigated machine learning techniques for detecting micrographia—abnormally small handwriting characteristic of early-stage Parkinson's disease. Research questions focused on developing real-time, automatic diagnostic capabilities using handwriting image analysis. Researchers utilized drawing samples from two open-source datasets to train models for micrographia detection. The machine learning model achieved 94% predictive accuracy, demonstrating high performance in identifying this early PD indicator. Key findings showed that micrographia features could reliably distinguish PD patients from healthy controls. The study also established foundations for a publicly accessible web portal enabling individuals to perform early PD screening through handwriting analysis.

**Relevance to Proposal (150-200 words):**
This research is exceptionally relevant to your thesis as it focuses specifically on micrographia detection, which represents a key manifestation of handwriting changes in Parkinson's disease severity progression. The study introduces and explains the concept of micrographia as a quantifiable digital biomarker, providing foundational knowledge for your severity assessment models. The emphasis on early-stage detection aligns with your goal of developing tools that can assess disease severity across different stages, potentially enabling monitoring of disease progression over time. The research demonstrates methods for extracting specific handwriting pathology features that could be integrated into your comprehensive severity assessment framework. The 94% accuracy achievement establishes a strong performance benchmark and validates the feasibility of automated handwriting analysis for PD assessment. The study addresses practical implementation considerations by developing a web-based diagnostic tool, offering insights into the translational aspects of your research and potential real-world applications. The focus on real-time, automatic diagnosis provides methodological approaches for developing efficient, clinically practical severity assessment tools. This work also demonstrates how machine learning can be applied to detect subtle motor changes that might not be apparent through traditional clinical observation.

---

## Summary

These five articles provide a comprehensive foundation for developing machine learning models for handwriting and drawing-based Parkinson's disease severity assessment. They collectively address key methodological approaches (CNNs, hybrid networks, feature extraction), important clinical concepts (micrographia, spiral/wave patterns), innovative data representation techniques (time-series-to-image conversion), and practical implementation considerations (cross-domain validation, real-time diagnosis). The research establishes strong performance benchmarks and provides multiple avenues for advancing the field of automated PD assessment through handwriting analysis.