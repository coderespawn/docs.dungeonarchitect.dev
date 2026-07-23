import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from './index.module.css';

const ENGINES = [
  {
    key: 'unreal',
    name: 'Unreal Engine',
    to: '/unreal/unreal-overview',
  },
  {
    key: 'unity',
    name: 'Unity',
    to: '/unity/unity-overview',
  },
];

export default function Home() {
  return (
    <Layout
      title="Documentation"
      description="Dungeon Architect documentation for Unreal Engine and Unity — setup guides and feature walkthroughs.">
      <main className={styles.page}>
        <div className={styles.hero}>
          <img src="/img/pixel-logo.png" alt="" className={styles.logo} />
          <div className={styles.eyebrow}>DOCUMENTATION</div>
          <Heading as="h1" className={styles.title}>
            Dungeon Architect Docs
          </Heading>
          <p className={styles.subtitle}>
            Setup, builders, the theme engine and more — for Unreal Engine and Unity. Pick your
            engine.
          </p>

          <div className={styles.engineGrid}>
            {ENGINES.map((e) => (
              <Link key={e.key} to={e.to} className={styles.engineCard}>
                <div className={styles.engineName}>{e.name}</div>
                <span className={styles.engineCta}>View documentation →</span>
              </Link>
            ))}
          </div>

          <div className={styles.backRow}>
            <a href="https://dungeonarchitect.dev" className={styles.backLink}>
              ← dungeonarchitect.dev
            </a>
          </div>
        </div>
      </main>
    </Layout>
  );
}
