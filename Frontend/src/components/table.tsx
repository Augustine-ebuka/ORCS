import React from 'react';
import '../styles/table.css'

interface Course {
  code: string;
  title: string;
  credit: number;
  grade: string;
  gradePoint: number;
}

interface CourseTableProps {
  courses: Course[];
}

const CourseTable: React.FC<CourseTableProps> = ({ courses }) => {
  const totalCreditPoints = courses.reduce((total, course) => total + course.gradePoint * course.credit, 0);
  const totalCredits = courses.reduce((total, course) => total + course.credit, 0);
  const cgpa = totalCreditPoints / totalCredits;

  return (
    <table className="course-table">
      <thead>
        <tr>
          <th className="course-table-header">Course Code</th>
          <th className="course-table-header">Course Title</th>
          <th className="course-table-header">Credit</th>
          <th className="course-table-header">Grade</th>
          <th className="course-table-header">Grade Point</th>
        </tr>
      </thead>
      <tbody>
        {courses.map((course, index) => (
          <tr key={index}>
            <td>{course.code}</td>
            <td>{course.title}</td>
            <td>{course.credit}</td>
            <td>{course.grade}</td>
            <td>{course.gradePoint}</td>
          </tr>
        ))}
       
        {/* <tr> */}
          {/* <td ></td>
          <td className="course-table-total">Total Credits:</td>
          <td className="course-table-total">{totalCredits}</td>
          <td className="course-table-total">CGPA:</td>
          <td className="course-table-total">{cgpa.toFixed(2)}</td>
        </tr>
        <tr>
          <td colSpan={2}></td>
          <td className="course-table-total" colSpan={4}>
            Total Credit Requirement: 120
          </td>
        </tr> */}
      </tbody>
      <div>
        
      </div>
    </table>
  );
};

export default CourseTable;