import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className={styles.title}>
          {siteConfig.title}
        </Heading>
        <p className={styles.subtitle}>{siteConfig.tagline}</p>
        <div className={styles.buttonRow}>
          <Link className={clsx('button button--lg', styles.primaryCta)} to="/unreal/unreal-overview">
            Unreal Documentation
          </Link>
          <Link className={clsx('button button--lg', styles.secondaryCta)} to="/unity/unity-overview">
            Unity Documentation
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout title={siteConfig.title} description={siteConfig.tagline}>
      <HomepageHeader />
      <main className={styles.mainSection}>
        <div className="container">
          <Heading as="h2" className={styles.mainHeading}>
            Build procedural worlds with Dungeon Architect
          </Heading>
          <p className={styles.mainCopy}>
            Browse setup guides, feature walkthroughs, and API docs tailored for Unreal Engine and Unity.
          </p>
        </div>
      </main>
    </Layout>
  );
}
