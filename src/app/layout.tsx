import type { Metadata } from 'next';
import { Inter_Tight } from 'next/font/google';
import './globals.css';

const interTight = Inter_Tight({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Data Universe | Bittensor Subnet',
  description: 'The quantum entanglement of the cosmos. A bittensor subnet visualization.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={interTight.className}>{children}</body>
    </html>
  );
}
