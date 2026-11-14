/**
 * ECK-056: carrier-specific plateau recovery with proposal-cost accounting.
 * Usage: node eck/test_eck056.cjs
 * Executes source neural definitions only; never evaluates final-test predictions.
 */
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const html=fs.readFileSync(path.join(__dirname,'index.html'),'utf8');
const source=html.split('<script>')[1].split('</script>')[0];
new Function(source);
const bounds=[
 ['const spinorStages=','function iterateSpinorSlot()'],
 ['const neuralCarrierNames=','function renderNeuralCarriers()'],
 ['const tripleCases=','function drawTripleNet()'],
 ['const temporalState=','function renderTemporal()'],
 ['const adaptState=','function adaptRender()'],
 ['const forgeEdges=','function renderForge()'],
 ['const collisionState=','function collisionRender()'],
 ['const dgState=','function dgRender()'],
 ['const plateauSpec=','function plateauRender()']
];
const snippets=bounds.map(([start,end])=>{
 const i=source.indexOf(start),j=source.indexOf(end,i);
 assert.ok(i>=0&&j>i,start);
 return source.slice(i,j);
}).join('\n');
const context=vm.createContext({});
vm.runInContext(snippets,context);
const report=vm.runInContext('plateauCompute()',context);
assert.equal(report.passed,true);
assert.equal(report.spent,40);
assert.equal(report.accepted,13);
assert.equal(report.rejected,27);
assert.equal(report.termination,'BUDGET_EXHAUSTED');
assert.equal(report.stalls.length,2);
assert.deepEqual(Array.from(report.stalls,s=>s.version),[7,8]);
assert.deepEqual(Array.from(report.stalls,s=>s.afterProposals),[22,32]);
assert.deepEqual(Array.from(report.recoveries,r=>r.block),['weak','fusion']);
assert.deepEqual(Array.from(report.recoveries,r=>r.rate),[70,70]);
assert.deepEqual(Array.from(report.recoveries,r=>r.fromVersion),[7,8]);
assert.deepEqual(Array.from(report.recoveries,r=>r.toVersion),[8,9]);
assert.equal(report.checkpoints.length,14);
assert.equal(report.test,'WITHHELD');
assert.equal(report.singlet,'(0=-.)');
for(let i=1;i<report.checkpoints.length;i++){
 const a=report.checkpoints[i-1],b=report.checkpoints[i];
 assert.equal(b.version,a.version+1);
 assert.ok(b.metrics.train<a.metrics.train);
 assert.ok(b.metrics.validation<=a.metrics.validation+1e-12);
 assert.ok(b.metrics.repeated<=a.metrics.repeated+1e-12);
 assert.ok(b.metrics.distinct<=a.metrics.distinct+1e-12);
}
assert.ok(Math.abs(report.final.validation-0.00003777177241941231)<1e-12);
assert.ok(Math.abs(report.final.repeated-0.00010624327505296336)<1e-12);
assert.ok(Math.abs(report.final.distinct-0.000008235045793174659)<1e-12);
assert.equal(vm.runInContext('tripleTrain.length',context),438);
assert.equal(vm.runInContext('tripleValid.length',context),146);
assert.equal(vm.runInContext('tripleTest.length',context),145);
console.log('ECK-056 PASS: recovered WEAK at 7->8, FUSION at 8->9; 13 accepted / 27 rejected / 40 proposals; test sealed.');
