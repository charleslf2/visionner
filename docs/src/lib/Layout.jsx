import React from 'react'
import styles from "../styles/Layout.module.css"
import Showcase_card from './Showcase_card'
import DatasetImporter from '../assets/screenshoot/DatasetImporter.png'
import SupervisedImporter from '../assets/screenshoot/SupervisedImporter.png'
import TrainTestSpliter from "../assets/screenshoot/TrainTestSpliter.png"
import DatasetNormalizer from '../assets/screenshoot/DatasetNormalizer.png'
import DatasetSaver from '../assets/screenshoot/DatasetSaver.png'
import DatasetOpener from '../assets/screenshoot/DatasetOpener.png'
import VisualizeImage from '../assets/screenshoot/VisualizeImage.png'


const Layout = () => {

  return (
    <div className={styles.wrapper}>
        
        <div className={styles.container}>

            <div className={styles.title}>What visionner can do for you ?</div>

            <div className={styles.showcase_container}>

                <div className={styles.showcase_01}>

                    <Showcase_card 
                    title="👉 Get your image folder ready for 
                    unsupervised computer vision taks in 2 lines of codes 👈 "
                    src={DatasetImporter}
                    />

                    <Showcase_card
                    title="👀 Visualize the first image in your imported dataset 👀"

                    src={VisualizeImage}
                    />

                </div>

                <div className={styles.showcase_02}>

                    <Showcase_card 
                    title="🤲 Split your dataset into Trainset and 
                    Testset in 2 lines of codes 🤲"

                    src={TrainTestSpliter}
                    />

                    <Showcase_card
                    title="👄 Normalized your dataset in 2 lines of codes 👄"
                    src={DatasetNormalizer}
                    />
                    
                </div>

                <div className={styles.showcase_03}>
                    
                    <Showcase_card
                    title="👌 Save your dataset in 2 lines of codes 👌"
                    src={DatasetSaver}
                    />
                    
                    <Showcase_card
                    title="🥽 Open your dataset in 2 lines of codes 🥽"
                    src={DatasetOpener}
                    />
                </div>

                <div className={styles.showcase_04}>
                    <Showcase_card
                        title="👩🏻‍💻 Get your image folder ready for 
                        supervised computer vision tasks in 2 lines of code 👩🏻‍💻 "

                        src={SupervisedImporter}
                    />
                </div>

            </div>
        </div>
    </div>

    
  )
}

export default Layout