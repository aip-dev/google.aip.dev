const assert = require('assert');
const yaml = require('js-yaml');
const fs = require('fs');
const path = require('path');
const Ajv = require('ajv');

const schemas = [
  '../assets/schema/nav-components.yaml',
  '../assets/schema/staticGroup.yaml',
  '../assets/schema/nav-schema.yaml',
];

function loadSchema(src) {
  console.log(`loading schema ${src}`);
  return yaml.safeLoad(fs.readFileSync(path.resolve(__dirname, src)));
}

function validator(schemas) {
  console.log(`schems list = ${JSON.stringify(schemas)}`);
  console.log(
    `sliced = ${JSON.stringify(schemas.slice(0, schemas.length - 1))}`
  );
  const ajv = schemas
    .slice(0, schemas.length - 1)
    .reduce((acc, s) => acc.addSchema(loadSchema(s)), new Ajv());
  console.log(`create validator with ${schemas[schemas.length - 1]}`);
  const validator = ajv.compile(loadSchema(schemas[schemas.length - 1]));

  return function(file) {
    console.log(`loading file from ${file}...`);
    const data = yaml.safeLoad(fs.readFileSync(path.resolve(__dirname, file)));
    const result = validator(data);
    if (validator.errors) console.log(validator.errors);
    assert(result);
  };
}

describe('nav.yaml', () => {
  const navValidation = validator(schemas);
  it('should conform to the nav-schema', () => {
    navValidation('../_data/nav.yaml');
  });
});

describe('header.yaml', () => {
  const headerValidation = validator(schemas.slice(0, schemas.length - 2));
  it('should conform to the staticMenuDef schema', () => {
    headerValidation('../_data/header.yaml');
  });
});
