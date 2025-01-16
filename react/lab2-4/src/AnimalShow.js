import bird from './svg/bird.svg';
import cat from './svg/cat.svg';
import cow from './svg/cow.svg';
import dog from './svg/dog.svg';
import gator from './svg/gator.svg';
import heart from './svg/heart.svg';
import horse from './svg/horse.svg';

import { useState } from 'react';
import './AnimalShow.css';

const svgMap = {
  bird: bird,
  cat: cat,
  cow: cow,
  dog: dog,
  gator: gator,
  heart: heart,
  horse: horse,
};

export default function AnimalShow({type}) {
  const animalSvg = svgMap[type];
  const [clicks, setClicks] = useState(0);

  const handleClick = () => {
    setClicks(clicks + 1);
  };

  return (
    <div className="animal-show">
      <img className="animal" alt="animal" src={animalSvg} />
      <img className="heart" alt="heart" src={heart} onClick={handleClick} style={{width: 20 + 10*clicks + 'px'}}/>
    </div>
  );
}
