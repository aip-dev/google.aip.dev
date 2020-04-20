const assert = require('assert');
const yaml = require('js-yaml');
const fs = require('fs');
const path = require('path');
const Ajv = require('ajv');

const schemata = [
  './schema/nav-components.yaml',
  './schema/static-group.yaml',
  './schema/nav-schema.yaml',
];

function loadSchema(src) {
  console.log(`loading schema ${src}`);
  return yaml.safeLoad(fs.readFileSync(path.resolve(__dirname, src)));
}

function validator(schemata) {
  console.log(`schems list = ${JSON.stringify(schemata)}`);
  console.log(
    `sliced = ${JSON.stringify(schemata.slice(0, schemata.length - 1))}`
  );
  const ajv = schemata
    .slice(0, schemata.length - 1)
    .reduce((acc, s) => acc.addSchema(loadSchema(s)), new Ajv());
  console.log(`create validator with ${schemata[schemata.length - 1]}`);
  const validator = ajv.compile(loadSchema(schemata[schemata.length - 1]));

  return function (file) {
    console.log(`loading file from ${file}...`);
    const data = yaml.safeLoad(fs.readFileSync(path.resolve(__dirname, file)));
    const result = validator(data);
    if (validator.errors) console.log(validator.errors);
    assert(result);
  };
}

describe('nav.yaml', () => {
  const navValidation = validator(schemata);
  it('should conform to the nav-schema', () => {
    navValidation('../_data/nav.yaml');
  });
});

describe('header.yaml', () => {
  const headerValidation = validator(schemata.slice(0, schemata.length - 2));
  it('should conform to the staticMenuDef schema', () => {
    headerValidation('../_data/header.yaml');
  });
});
