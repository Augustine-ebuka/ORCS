import Button from "../components/button"
import InputForm from "../components/input"
import Layout from "../components/layout"
import '../styles/login.css'

function Login() {
    

    return (
        <>
            <Layout>
                <div className="login_container">
                    <h1>Student Login</h1>
                    <form method="POST">
                        <InputForm inputName="matric_no" inputType='text' label="Matric No" placeholder="e.g FAT/17/2473"></InputForm>
                        <InputForm inputName="Password" inputType='password' label="password" placeholder="password"></InputForm>
                        <Button buttonName="submit"></Button>
                    </form>
                </div>
            </Layout>
        </>
    )
}

export default Login