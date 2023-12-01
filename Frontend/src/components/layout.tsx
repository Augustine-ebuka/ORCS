import '../styles/layout.css';
import { FC, ReactNode } from 'react';

interface LayoutProps {
  children: ReactNode;
  leftmargin?: string | number | undefined;
  rightmargin: string | number;
  topmargin?: string | number;
  bottommargin?: string | number;
}

const Layout: FC<LayoutProps> = ({ children, leftmargin, rightmargin, topmargin, bottommargin }) => {
  return (
    <>
      <div
        className="layout"
        style={{
          marginLeft: leftmargin,
          marginRight: rightmargin,
          marginTop: topmargin,
          marginBottom: bottommargin,
        }}
      >
        {children}
      </div>
    </>
  );
};

export default Layout;