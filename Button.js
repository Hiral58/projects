// Button.js

import React from 'react';

function Button(props) {
  const handleButtonClick = () => {
    // Raise a custom event by calling a function passed via props
    props.onCustomClick('Button clicked!');
  };

  return (
    <button onClick={handleButtonClick}>Click me</button>
  );
}

export default Button;
