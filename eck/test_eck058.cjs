/**
 * ECK-058: seeded robustness and validation-screening cost regression.
 * Run: node eck/test_eck058.cjs
 * Extract actual model functions from eck/index.html; 145 final-test cases unopened.
 */
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
const script=html.split('<script>')[1].split('</script>')[0];
assert.ok(script,'HTML neural script present');
new Function(script);
const boundaries=[
 ['const spinorStages=','function iterateSpinorSlot()'],
 ['const neuralCarrierNames=','function renderNeuralCarriers()'],
 ['const tripleCases=','function drawTripleNet()'],
 ['const temporalState=','function renderTemporal()'],
 ['const adaptState=','function adaptRender()'],
 ['const forgeEdges=','function renderForge()'],
 ['const nState=','function nRender()'],
 ['const shiftState=','function shiftRender()'],
 ['const seedLab=','function renderSeedLab()'],
 ['const collisionState=','function collisionRender()'],
 ['const dgState=','function dgRender()'],
 ['const rankSpec=','function rankRender()'],
 ['const robustSpec=','function robustRender()']
];
const sections=boundaries.map(([start,end])=>{
 const i=script.indexOf(start),j=script.indexOf(end,i);
 assert.ok(i>=0&&j>i,'model section '+start);
 return script.slice(i,j);
});
const context=vm.createContext({});
vm.runInContext(sections.join('\n')+'\nfunction robustRender(){}',context);
const report=vm.runInContext('robustCompare()',context);
assert.equal(report.passed,true);
assert.equal(report.runs.length,9);
const by=(seed,policy)=>report.runs.find(r=>r.seed===seed&&r.policy===policy);
for(const seed of [0,1,2]){
 const fixed=by(seed,'fixed'),ranked=by(seed,'ranked'),gradient=by(seed,'gradient');
 assert.ok(fixed&&ranked&&gradient);
 for(const run of [fixed,ranked,gradient]){
  assert.equal(run.proposals,40);
  assert.equal(run.proposals,run.accepted+run.rejected);
  assert.equal(run.checkpoints.length,run.accepted+1);
  assert.equal(run.test,'WITHHELD');
  assert.equal(run.singlet,'(0=-.)');
  assert.ok(Number.isFinite(run.shifted));
  for(let i=1;i<run.checkpoints.length;i++){
   const before=run.checkpoints[i-1].metrics,after=run.checkpoints[i].metrics;
   assert.ok(after.train<before.train,'training improves');
   assert.ok(after.validation<=before.validation+1e-12,'aggregate nonworsening');
   assert.ok(after.repeated<=before.repeated+1e-12,'repeat cohort nonworsening');
   assert.ok(after.distinct<=before.distinct+1e-12,'distinct cohort nonworsening');
  }
 }
 assert.equal(ranked.selections[0].block,'fusion');
 assert.equal(ranked.selections[0].probes,5);
 assert.equal(gradient.selections[0].block,'fusion');
 assert.equal(gradient.selections[0].probes,1);
 assert.equal(gradient.gradientScoreCalls,1);
 assert.equal(fixed.selections[0].block,'weak');
 assert.equal(fixed.selections[0].probes,1);
}
assert.ok(by(0,'gradient').metrics.validation<by(0,'fixed').metrics.validation);
assert.ok(by(1,'fixed').metrics.validation<by(1,'gradient').metrics.validation);
assert.ok(by(2,'fixed').metrics.validation<by(2,'gradient').metrics.validation);
assert.equal(vm.runInContext('tripleTrain.length',context),438);
assert.equal(vm.runInContext('tripleValid.length',context),146);
assert.equal(vm.runInContext('tripleTest.length',context),145);
assert.equal(vm.runInContext('dgState.final',context),null);
console.log('ECK-058 PASS: nine seeded comparisons; fixed/ranked/gradient; 40 candidates each.');
for(const policy of ['fixed','ranked','gradient']){
 const rows=report.runs.filter(x=>x.policy===policy);
 const mean=rows.reduce((sum,x)=>sum+x.metrics.validation,0)/rows.length;
 const shift=rows.reduce((sum,x)=>sum+x.shifted,0)/rows.length;
 console.log(policy,'validation',mean,'zero-shot changed target',shift,
  'accepted',rows.map(x=>x.accepted).join('/'));
}
console.log('Final 145 cases withheld.');
