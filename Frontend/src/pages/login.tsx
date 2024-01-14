import { useState } from "react";
import Button from "../components/button";
import InputForm from "../components/input";
import Layout from "../components/layout";
import '../styles/login.css';
import httpClient from "../components/httpClient";
import {useNavigate } from "react-router-dom";
import { ToastContainer, toast } from 'react-toastify';

function Login() {
  const [formData, setFormData] = useState({
    matric_no: '',
    password: ''
  });
  const navigate = useNavigate()

  const login = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    if (!validateForm()) {
      return;
    }

    const api = 'http://localhost:5000/api/student/login';
    try {
      const result = await httpClient.post(api, formData);
      if (result.status == 200) {
        toast.success("login success");

        setTimeout(() => {
            navigate('/student/dashboard')
            
        }, 3000);
        console.log(result.data);
      }
    } 
    catch (error:any) {
        switch (error.response.status) {
            case 404:
              toast.error("user doesnt exist!");
              break;
    
            case 401:
              toast.error("password or matric no cannot be empty");
              break
    
            case 500:
              toast.error("server error");
              break
    
            default:
              toast.error("something went wrong");
              break;
          }
      console.error("API call error:", error);
    }
  };

  const handleSubmit = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const validateForm = () => {
    const { matric_no, password } = formData;

    if (matric_no.trim() === '' || password.trim() === '') {
      toast.error('Please fill in all required fields');
      return false;
    }

    return true;
  };

  return (
    <>
      <ToastContainer></ToastContainer>
      <Layout leftmargin={15} rightmargin={15}>
        <div className="login_container">
          <h1>Student Login</h1>
          <form method="POST" className="login_form" onSubmit={login}>
            <InputForm
              inputName="matric_no"
              inputType='text'
              label="Matric No"
              onChange={handleSubmit}
              placeholder="e.g FAT/17/2473"
            ></InputForm>
            <InputForm
              inputName="password"
              inputType='password'
              label="password"
              onChange={handleSubmit}
              placeholder="password"
            ></InputForm>
            <Button buttonName="submit"></Button>
          </form>
        </div>
      </Layout>
    </>
  );
}

export default Login;
