const assert = require('assert')
const yaml = require('js-yaml')
const fs = require('fs')
const path = require('path')
const Ajv = require('ajv')

function validator(schemaSrc) {
  const schema = yaml.safeLoad(fs.readFileSync(path.resolve(__dirname, schemaSrc)))
  const ajv = new Ajv({schemaId: 'id'})
  ajv.addMetaSchema(require('ajv/lib/refs/json-schema-draft-04.json'))
  const validator = ajv.compile(schema)
  
  return function(file) {
    console.log(`loading file from ${file}...`)
    const data = yaml.safeLoad(fs.readFileSync(path.resolve(__dirname, file)))
    
    assert(validator(data))
  }
}

describe('nav.yaml', () => {
  const navValidation = validator('../assets/schema/nav-schema.yaml')
  it('should conform to the nav-schema', () => {
    navValidation('../_data/nav.yaml')
  })
})

