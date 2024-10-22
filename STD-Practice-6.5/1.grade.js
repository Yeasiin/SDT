function calculate_grade(marks) {
  let grade;
  if (marks >= 80 && marks <= 100) {
    grade = "A+";
  } else if (marks >= 70 && marks < 80) {
    grade = "A";
  } else if (marks >= 60 && marks < 70) {
    grade = "A-";
  } else if (marks >= 50 && marks < 60) {
    grade = "B";
  } else if (marks >= 40 && marks < 50) {
    grade = "C";
  } else if (marks >= 33 && marks < 40) {
    grade = "D";
  } else {
    grade = "F";
  }

  console.log(`You Got ${grade} for Your ${marks}`);
}

calculate_grade(59);
calculate_grade(79);
calculate_grade(80);
