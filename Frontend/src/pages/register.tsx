import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import {Blocks} from 'react-loader-spinner'

import Button from '../components/button';
import InputForm from '../components/input';
import Layout from '../components/layout';
import { useNavigate } from 'react-router-dom';

import '../styles/register.css';

function Register() {
  const faculty = ['SOS', 'SOC', 'PLD'];
  const department = ['software engineering', 'computer science', 'information technology'];
  const level = ['100', '200', '300', '400', '500'];
  const api = 'http://localhost:5000/api/student/register';
  const navigate = useNavigate()
  const [formData, setFormData] = useState({
    first_name: '',
    middle_name: '',
    last_name: '',
    faculty: '',
    department: '',
    image: '',
    matric_no: '',
    level: '',
    password: ''
  });
  const [loading, setIsloading] = useState<boolean>()

  const formSubmit = async (event:any) => {
    event.preventDefault();
    if (!validateForm()) {
      return;
    }
    try {
      const result = await axios.post(api, formData);
      setIsloading(true)
      setTimeout(() => {
        navigate('/register')
      }, 3000);
     if(result.status == 201){
      toast.success("registration created!");
     }
    } 
    catch (error:any) {
      switch (error.response.status) {
        case 403:
          toast.error("user already exist!");
          break;

        case 400:
          toast.error("missing field(s)!");
          break

        case 500:
          toast.error("server error");
          break

        default:
          toast.error("something went wrong");
          break;
      }
      console.log(error.response.status);
    } 
    finally{
      setIsloading(false)
      console.log('i am done regardless')
    }
  };

  const handleSubmit = (event:any) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const validateForm = () => {
    const {
      first_name,
      middle_name,
      last_name,
      faculty,
      department,
      matric_no,
      level,
      password
    } = formData;

    if (
      first_name.trim() === '' ||
      middle_name.trim() === '' ||
      last_name.trim() === '' ||
      faculty.trim() === '' ||
      department.trim() === '' ||
      matric_no.trim() === '' ||
      level.trim() === '' ||
      password.trim() === ''
    ) {
      toast.error('Please fill in all required fields');
      return false;
    }
    return true;
  };

  return (
    <>
      <Layout leftmargin={150} rightmargin={150}>
        <ToastContainer />
 
        <form onSubmit={formSubmit}>
          <div className="register_container">
            <h1>Student details registration</h1>
            <div className="three_col">
              <InputForm
                inputName="first_name"
                inputType="text"
                placeholder="first name"
                label="first name"
                value={formData.first_name}
                onChange={handleSubmit}
              />
              <InputForm
                inputName="middle_name"
                inputType="text"
                placeholder="middle name"
                label="middle name"
                value={formData.middle_name}
                onChange={handleSubmit}
              />
              <InputForm
                inputName="last_name"
                inputType="text"
                placeholder="last name"
                label="last name"
                value={formData.last_name}
                onChange={handleSubmit}
              />
            </div>
            <div className="two_col">
              <InputForm
                inputName="matric_no"
                inputType="text"
                placeholder="matric number"
                label="matric No"
                value={formData.matric_no}
                onChange={handleSubmit}
              />
              <InputForm
                inputName="password"
                inputType="password"
                placeholder="password"
                label="password"
                value={formData.password}
                onChange={handleSubmit}
              />
            </div>
            <div className="two_col">
              <InputForm
                inputName="faculty"
                inputType="select"
                placeholder="Faculty"
                options={faculty}
                label="faculty"
                value={formData.faculty}
                onChange={handleSubmit}
              />
              <InputForm
                inputName="department"
                inputType="select"
                placeholder="department"
                value={formData.department}
                options={department}
                label="department"
                onChange={handleSubmit}
              />
            </div>
            <div className="two_col">
              <InputForm
                inputName="image"
                inputType="file"
                placeholder="image"
                label="image"
                value={formData.image}
                onChange={handleSubmit}
              />
              <InputForm
                inputName="level"
                inputType="select"
                placeholder="level"
                options={level}
                value={formData.level}
                label="level"
                onChange={handleSubmit}
              />
            </div>
            {loading?"hello":"nothing"}
            {loading && (
                     <Blocks
                     height="80"
                     width="80"
                     color="#4fa94d"
                     ariaLabel="blocks-loading"
                     wrapperStyle={{}}
                     wrapperClass="blocks-wrapper"
                     visible={true}
                     />
            )}
            <Button buttonName="submit details" />
          </div>
        </form>
      </Layout>
    </>
  );
}

export default Register;