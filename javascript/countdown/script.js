/* eslint-disable no-unused-vars */
function updateCounter() {
  const counter = document.getElementById("counter");

  const targetDate = new Date("2025-07-31");
  const currentDate = new Date();
  currentDate.setHours(0, 0, 0, 0);

  const timeDifference = targetDate - currentDate;
  const daysDifference = Math.ceil(timeDifference / (1000 * 60 * 60 * 24));

  counter.innerText = daysDifference;
}
