import React, { useState } from 'react';
import axios from 'axios';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import Button from '../components/button';
import InputForm from '../components/input';
import Layout from '../components/layout';

import '../styles/register.css';

function Register() {
  const faculty = ['SOS', 'SOC', 'PLD'];
  const department = ['SEN', 'CSC', 'IFT'];
  const level = ['100', '200', '300', '400', '500'];
  const api = 'http://localhost:5000/api/student/register';

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
  const [loading, setIsloading] = useState<boolean>(false)

  const formSubmit = async (event:any) => {
    event.preventDefault();
    if (!validateForm()) {
      return;
    }
    try {
      console.log(formData)
      const result = await axios.post(api, formData);
      setIsloading(true)
      if (result.data && result.data.data) {
        toast.success(result.data.data.message);
        console.log(result.data.data);
      } else {
        toast.error(result.data);
      }
    } catch (error:any) {
      toast.error(error.message);
      console.log(error);
    } finally{
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
      last_name,
      faculty,
      department,
      matric_no,
      level,
      password
    } = formData;

    if (
      first_name.trim() === '' ||
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
            {loading && <p>Loading...</p>}
            <Button buttonName="submit details" />
          </div>
        </form>
      </Layout>
    </>
  );
}

export default Register;