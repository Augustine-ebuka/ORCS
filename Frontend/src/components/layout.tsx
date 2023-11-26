import '../styles/layout.css'
import{ FC, ReactNode }from 'react'

interface LayoutProps{
    children: ReactNode
}
const Layout : FC<LayoutProps> = ({children})=> {

    return (
        <>
            <div className='layout'>
                {children}
            </div>
        </>
    )
}
export default Layout
