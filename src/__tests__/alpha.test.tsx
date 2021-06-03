import React from 'react';
import { mount } from 'enzyme';
import CategoryGallery from '../modules/category/CategoryGallery';

//Comments to help describe what I wanted to do.
/*
  I wanted to grab the state 'books' from inside of CategoryGallery and check that it is in alphabetical order
*/

test('renders the component', () => {
  const component = mount(<CategoryGallery match={'cooks'}/>);
  expect(component).toMatchSnapshot();
});

expect(books[]).toBeSortedBy('book.name');