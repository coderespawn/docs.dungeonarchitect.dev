// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Dungeon Architect Documentation',
  tagline: 'Choose your engine',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://docs.dungeonarchitect.dev',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'coderespawn', // Usually your GitHub org/user name.
  projectName: 'docs.dungeonarchitect.dev', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      colorMode: {
        defaultMode: 'dark',
        respectPrefersColorScheme: false,
      },
      navbar: {
        title: 'Dungeon Architect Docs',
        logo: {
          alt: 'Dungeon Architect',
          src: 'img/pixel-logo.png',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'unrealSidebar',
            position: 'left',
            label: 'Unreal',
          },
          {
            type: 'docSidebar',
            sidebarId: 'unitySidebar',
            position: 'left',
            label: 'Unity',
          },
          {
            href: 'https://dungeonarchitect.dev',
            label: 'Product',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Unreal',
                to: '/unreal/unreal-overview',
              },
              {
                label: 'Unity',
                to: '/unity/unity-overview',
              },
            ],
          },
          {
            title: 'Dungeon Architect',
            items: [
              {
                label: 'Product site',
                href: 'https://dungeonarchitect.dev',
              },
              {
                label: 'Video tutorials',
                to: '/unreal/video-tutorials',
              },
              {
                label: 'YouTube',
                href: 'https://www.youtube.com/@DungeonArchitectDev',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} CodeRespawn. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
  trailingSlash: true
};

export default config;

