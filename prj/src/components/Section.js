import styled from 'styled-components'
import { useState, useRef, useEffect, useCallback } from 'react'

let space = new Array(14);

for(var i=0; i<space.length; i++) {
  space[i] = new Array(5);
}

for(let i=0; i<5; i++)
  for(let j=0; j<14; j++)
    space[j][i] = null

const Th = styled.th`
  background-color: rgb(200, 200, 200);
  height: 5px;
`

const Td = styled.td`
  background-color: rgb(200, 200, 200);
  width: 5px;
`

function Section() {
  const data = useRef([]);
  const [update, updating] = useState();

  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const id = urlParams.get('id');
  const list = urlParams.get('list');

  const get = useCallback(async () => {
    try {
      let response;

      if(list == "student")
        response = await fetch("http://127.0.0.1:5000/api/lecture_list_student/" + id)
      else if(list == "professor")
        response = await fetch("http://127.0.0.1:5000/api/lecture_list_professor/" + id)

      if(!response.ok) throw 'Something went wrong!';
      const datas = await response.json();

      console.log(datas)

      let value = datas.map (
        function(jsonElem) {
          return {
            'course_name': jsonElem['course_name'],
            'credit': jsonElem['credit'],
            'day': jsonElem['day'],
            'professor_major': jsonElem['professor_major'],
            'professor_name': jsonElem['professor_name'],
            'start_time': jsonElem['start_time'],
            'end_time': jsonElem['end_time'],
          }
        }
      )

      data.current = value

      await updating(0)

    } catch(e) {
      console.log(e)
    }
  }, []);

  function set() {
    try {
      for(var i = 0; data.current[i] != null; i++)
      {
        let startTime = data.current[i].start_time.split(':')[0] - 1
        let credit = data.current[i].credit
        let courseName = data.current[i].course_name
        let professor = data.current[i].professor_name

        let dayToNum = {'월요일': 0, '화요일': 1, '수요일': 2, '목요일': 3, '금요일': 4}
        let day = dayToNum[data.current[i].day]

        let start = startTime - 8

        for(let i=1; i<credit; i++)
          space[start + i][day] = undefined;

        let red, green, blue;

        red = Math.ceil(Math.random() * 200);
        green = Math.ceil(Math.random() * 200);
        blue = Math.ceil(Math.random() * 200);
        
        const Td = styled.td`
          background-color: rgb(${red}, ${green}, ${blue});
          color: white;
        `
        
        space[start][day] = <Td rowSpan={credit}>{courseName}<br />[{professor}]</Td>
      }

    } catch(e) {
      console.log(e)
    }
  }

  function clean() {
    let ar = new Array(14);
    let p = [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

    for(let i=0; i<14; i++)
    {
      ar[i] = <tr> 
                <Td>{p[i]}</Td>
                {space[i].map((val) => {
                return (
                  val === null ? <td></td> : val
                )
                })} 
              </tr>
    }

    return (
      <table border='1'>
        <tr>
          <Th></Th>
          <Th>월</Th>
          <Th>화</Th>
          <Th>수</Th>
          <Th>목</Th>
          <Th>금</Th>
        </tr>
        {ar}
      </table>
    )
  }

  useEffect(() => {get()}, [])

  return (
    <div className="Section">
      <form>
        <select id="list" name="list">
          <option value="student" selected={list === "student"}>수강 목록</option>
          <option value="professor" selected={list === "professor"}>교수 강의 목록</option>
        </select>
        <input type="text" name="id" placeholder="학생/교수 아이디" />
        <button type="submit">확인</button>
      </form>
      {set()}
      {clean()}
    </div>
  );
}

export default Section;