/* 1Each.com — calculators. Pure client-side, no data leaves the browser. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function st(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  var cur = st("cur") || "USD";
  function money(n) { if (!isFinite(n)) n = 0; try { return new Intl.NumberFormat(undefined, { style: "currency", currency: cur }).format(n); } catch (e) { return "$" + n.toFixed(2); } }
  function num(el) { var v = parseFloat(typeof el === "string" ? el : el && el.value); return isFinite(v) ? v : 0; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  /* currency selector */
  $$(".cur-select").forEach(function (s) {
    s.value = cur;
    s.addEventListener("change", function () { cur = s.value; st("cur", cur); $$(".cur-select").forEach(function (x) { x.value = cur; }); document.dispatchEvent(new Event("recalc")); });
  });
  function live(root, fn) { root.addEventListener("input", fn); root.addEventListener("change", fn); document.addEventListener("recalc", fn); fn(); }
  function chips(root, input) {
    $$(".chip", root).forEach(function (c) { c.addEventListener("click", function () { $$(".chip", root).forEach(function (x) { x.classList.remove("active"); }); c.classList.add("active"); input.value = c.getAttribute("data-v"); input.dispatchEvent(new Event("input", { bubbles: true })); }); });
  }

  /* ---------- Hero quick split ---------- */
  var h = $("#hero-split");
  if (h) {
    chips($("#hs-tips"), $("#hs-tip"));
    live(h, function () {
      var bill = num($("#hs-bill")), ppl = Math.max(1, Math.round(num($("#hs-people")))), tip = num($("#hs-tip"));
      var total = bill * (1 + tip / 100);
      $("#hs-each").textContent = money(total / ppl);
      $("#hs-sub").textContent = money(total) + " total · " + money(bill * tip / 100) + " tip · " + ppl + " people";
    });
  }

  /* ---------- Split bill ---------- */
  var sb = $("#tool-split");
  if (sb) {
    var mode = "equal";
    $$(".seg button", sb).forEach(function (b) { b.addEventListener("click", function () {
      $$(".seg button", sb).forEach(function (x) { x.classList.remove("active"); }); b.classList.add("active"); mode = b.getAttribute("data-mode");
      $("#sb-equal").style.display = mode === "equal" ? "" : "none"; $("#sb-items").style.display = mode === "items" ? "" : "none"; calc(); }); });
    chips($("#sb-tips"), $("#sb-tip"));
    var list = $("#sb-people");
    var addP = function (n, a) {
      var d = document.createElement("div"); d.className = "item-row people";
      d.innerHTML = '<input placeholder="Name" value="' + esc(n || "") + '" aria-label="Name"><input type="number" min="0" step="0.01" placeholder="Their items" value="' + (a || "") + '" aria-label="Their items"><button type="button" class="rm" aria-label="Remove">×</button>';
      $(".rm", d).onclick = function () { d.remove(); calc(); }; list.appendChild(d);
    };
    ["Alex", "Sam", "Jordan"].forEach(function (n, i) { addP(n, [24, 31.5, 18][i]); });
    $("#sb-add").onclick = function () { addP("", ""); calc(); };
    var calc = function () {
      var tax = num($("#sb-tax")), tip = num($("#sb-tip")), tipPre = $("#sb-tippre").checked, round = $("#sb-round").checked, out = $("#sb-out"), work = $("#sb-work");
      if (mode === "equal") {
        var sub = num($("#sb-bill")), ppl = Math.max(1, Math.round(num($("#sb-ppl"))));
        var taxA = sub * tax / 100, tipA = (tipPre ? sub : sub + taxA) * tip / 100, total = sub + taxA + tipA, each = total / ppl;
        if (round) each = Math.ceil(each);
        $("#sb-each").textContent = money(each);
        out.innerHTML = "<tr><td>Subtotal</td><td>" + money(sub) + "</td></tr><tr><td>Tax (" + tax + "%)</td><td>" + money(taxA) + "</td></tr><tr><td>Tip (" + tip + "%)</td><td>" + money(tipA) + "</td></tr><tr><td>Total</td><td>" + money(total) + "</td></tr>" + (round ? "<tr><td>Collected (rounded up)</td><td>" + money(each * ppl) + "</td></tr>" : "");
        work.textContent = "Tax  = " + sub.toFixed(2) + " × " + tax + "% = " + taxA.toFixed(2) + "\nTip  = " + (tipPre ? sub : sub + taxA).toFixed(2) + " × " + tip + "% = " + tipA.toFixed(2) + "\nEach = (" + sub.toFixed(2) + " + " + taxA.toFixed(2) + " + " + tipA.toFixed(2) + ") ÷ " + ppl + " = " + (total / ppl).toFixed(2);
      } else {
        var rows = $$(".item-row", list), shared = num($("#sb-shared")), n = Math.max(1, rows.length), itemsSum = 0;
        rows.forEach(function (r) { itemsSum += num($$("input", r)[1]); });
        var subT = itemsSum + shared, mult = 1 + tax / 100 + (tipPre ? tip / 100 : (1 + tax / 100) * tip / 100 - 0);
        if (!tipPre) mult = (1 + tax / 100) * (1 + tip / 100);
        var html = "", grand = 0;
        rows.forEach(function (r) {
          var ins = $$("input", r), mine = num(ins[1]) + shared / n, pay = mine * mult; if (round) pay = Math.ceil(pay); grand += pay;
          html += "<tr><td>" + esc(ins[0].value || "Guest") + "</td><td>" + money(pay) + "</td></tr>";
        });
        $("#sb-each").textContent = money(grand / n) + " avg";
        out.innerHTML = html + "<tr><td>Grand total</td><td>" + money(grand) + "</td></tr>";
        work.textContent = "Shared " + shared.toFixed(2) + " ÷ " + n + " = " + (shared / n).toFixed(2) + " per person\nEach pays (own items + shared share) × " + mult.toFixed(4) + "\n(multiplier = tax " + tax + "% and tip " + tip + "% " + (tipPre ? "on pre-tax" : "on post-tax") + ")\nSubtotal " + subT.toFixed(2);
      }
    };
    live(sb, calc);
  }

  /* ---------- Unit price ---------- */
  var up = $("#tool-unit");
  if (up) {
    var U = { g: ["mass", 1], kg: ["mass", 1000], oz: ["mass", 28.3495], lb: ["mass", 453.592], ml: ["vol", 1], l: ["vol", 1000], floz: ["vol", 29.5735], gal: ["vol", 3785.41], ct: ["count", 1], sheet: ["count", 1], load: ["count", 1] };
    var label = { mass: ["100 g", 100], vol: ["100 ml", 100], count: ["1 each", 1] };
    var list2 = $("#up-items");
    var opts = Object.keys(U).map(function (k) { return '<option value="' + k + '">' + (k === "floz" ? "fl oz" : k) + "</option>"; }).join("");
    var addI = function (n, p, q, u) {
      var d = document.createElement("div"); d.className = "item-row";
      d.innerHTML = '<input placeholder="Item name" value="' + esc(n || "") + '" aria-label="Item"><input type="number" min="0" step="0.01" placeholder="Price" value="' + (p || "") + '" aria-label="Price"><div style="display:flex;gap:6px"><input type="number" min="0" step="any" placeholder="Qty" value="' + (q || "") + '" aria-label="Quantity"><select aria-label="Unit">' + opts + '</select></div><button type="button" class="rm" aria-label="Remove">×</button><div class="small muted up-r" style="grid-column:1/-1;margin-top:-4px"></div>';
      $("select", d).value = u || "g"; $(".rm", d).onclick = function () { d.remove(); calc2(); }; list2.appendChild(d);
    };
    addI("Small pack", 3.49, 400, "g"); addI("Family size", 5.99, 1, "kg"); addI("Bulk club", 14.99, 2.5, "kg");
    $("#up-add").onclick = function () { addI(); calc2(); };
    var calc2 = function () {
      var rows = $$(".item-row", list2), items = [];
      rows.forEach(function (r) {
        var ins = $$("input", r), p = num(ins[1]), q = num(ins[2]), u = $("select", r).value, base = q * U[u][1];
        r.classList.remove("best");
        if (p > 0 && base > 0) items.push({ r: r, n: ins[0].value || "Item", kind: U[u][0], per: p / base });
        else $(".up-r", r).textContent = "";
      });
      var kinds = {}; items.forEach(function (i) { kinds[i.kind] = true; });
      var out = $("#up-out");
      if (!items.length) { out.innerHTML = ""; $("#up-best").textContent = "—"; return; }
      if (Object.keys(kinds).length > 1) { $("#up-best").textContent = "Mixed units"; out.innerHTML = "<tr><td colspan=2>Compare weight with weight, volume with volume, or count with count.</td></tr>"; return; }
      var k = items[0].kind, L = label[k]; items.sort(function (a, b) { return a.per - b.per; });
      var best = items[0], worst = items[items.length - 1];
      best.r.classList.add("best");
      items.forEach(function (i) { $(".up-r", i.r).textContent = money(i.per * L[1]) + " per " + L[0] + (i === best ? "  ★ best value" : "  (+" + ((i.per / best.per - 1) * 100).toFixed(0) + "% vs best)"); });
      $("#up-best").textContent = best.n;
      out.innerHTML = items.map(function (i) { return "<tr><td>" + esc(i.n) + "</td><td>" + money(i.per * L[1]) + " / " + L[0] + "</td></tr>"; }).join("") +
        (items.length > 1 ? "<tr><td>Overpay on worst choice</td><td>" + ((worst.per / best.per - 1) * 100).toFixed(0) + "%</td></tr>" : "");
    };
    live(up, calc2);
  }

  /* ---------- Cost per use ---------- */
  var cpu = $("#tool-cpu");
  if (cpu) live(cpu, function () {
    var res = ["a", "b"].map(function (x) {
      var price = num($("#cpu-" + x + "-price")), per = num($("#cpu-" + x + "-uses")), yrs = num($("#cpu-" + x + "-years")), mnt = num($("#cpu-" + x + "-maint")), resale = num($("#cpu-" + x + "-resale"));
      var uses = per * 52 * yrs, cost = price + mnt * yrs - resale;
      return { name: $("#cpu-" + x + "-name").value || x.toUpperCase(), uses: uses, cost: cost, cpu: uses > 0 ? cost / uses : 0 };
    });
    var a = res[0], b = res[1], w = a.cpu <= b.cpu ? a : b, l = w === a ? b : a;
    $("#cpu-best").textContent = w.name;
    $("#cpu-out").innerHTML = res.map(function (r) { return "<tr><td>" + esc(r.name) + " — " + Math.round(r.uses) + " uses</td><td>" + money(r.cpu) + " / use</td></tr>"; }).join("") +
      "<tr><td>Saving per use</td><td>" + money(l.cpu - w.cpu) + "</td></tr><tr><td>Lifetime saving (at " + Math.round(w.uses) + " uses)</td><td>" + money((l.cpu - w.cpu) * w.uses) + "</td></tr>";
    $("#cpu-work").textContent = "Cost per use = (price + yearly upkeep × years − resale) ÷ (uses per week × 52 × years)\n" + res.map(function (r) { return r.name + ": " + r.cost.toFixed(2) + " ÷ " + Math.round(r.uses) + " = " + r.cpu.toFixed(3); }).join("\n");
  });

  /* ---------- Tip ---------- */
  var tp = $("#tool-tip");
  if (tp) { chips($("#tp-tips"), $("#tp-pct")); live(tp, function () {
    var bill = num($("#tp-bill")), pct = num($("#tp-pct")), ppl = Math.max(1, Math.round(num($("#tp-ppl")))), round = $("#tp-round").value;
    var tip = bill * pct / 100, total = bill + tip;
    if (round === "total") { total = Math.ceil(total); tip = total - bill; }
    var each = total / ppl; if (round === "each") { each = Math.ceil(each); total = each * ppl; tip = total - bill; }
    $("#tp-each").textContent = money(each);
    $("#tp-out").innerHTML = "<tr><td>Tip</td><td>" + money(tip) + " (" + (bill ? (tip / bill * 100).toFixed(1) : 0) + "%)</td></tr><tr><td>Total</td><td>" + money(total) + "</td></tr><tr><td>Tip each</td><td>" + money(tip / ppl) + "</td></tr>";
  }); }

  /* ---------- Group trip settle-up ---------- */
  var tr = $("#tool-trip");
  if (tr) {
    var ppl = ["Alex", "Sam", "Jordan", "Riya"], exps = [["Alex", 420, "Cabin"], ["Sam", 136.4, "Groceries"], ["Riya", 88, "Gas"], ["Alex", 54, "Dinner"]];
    var pWrap = $("#tr-people"), eWrap = $("#tr-exps");
    var renderP = function () {
      pWrap.innerHTML = ppl.map(function (p, i) { return '<span class="chip active" style="cursor:default">' + esc(p) + ' <button type="button" data-i="' + i + '" aria-label="Remove ' + esc(p) + '" style="border:0;background:none;color:inherit;cursor:pointer">×</button></span>'; }).join(" ");
      $$("button", pWrap).forEach(function (b) { b.onclick = function () { var n = ppl[b.dataset.i]; ppl.splice(b.dataset.i, 1); exps = exps.filter(function (e) { return e[0] !== n; }); renderE(); renderP(); calc3(); }; });
    };
    var renderE = function () {
      eWrap.innerHTML = exps.map(function (e, i) {
        return '<div class="item-row" data-i="' + i + '"><select aria-label="Paid by">' + ppl.map(function (p) { return "<option" + (p === e[0] ? " selected" : "") + ">" + esc(p) + "</option>"; }).join("") + '</select><input type="number" min="0" step="0.01" value="' + e[1] + '" aria-label="Amount"><input value="' + esc(e[2]) + '" placeholder="What for" aria-label="Description"><button type="button" class="rm" aria-label="Remove">×</button></div>';
      }).join("");
      $$(".item-row", eWrap).forEach(function (r) {
        var i = +r.dataset.i, f = $$("input,select", r);
        f[0].onchange = function () { exps[i][0] = f[0].value; calc3(); };
        f[1].oninput = function () { exps[i][1] = num(f[1]); calc3(); };
        f[2].oninput = function () { exps[i][2] = f[2].value; };
        $(".rm", r).onclick = function () { exps.splice(i, 1); renderE(); calc3(); };
      });
    };
    $("#tr-add-p").onclick = function () { var n = $("#tr-name").value.trim(); if (n && ppl.indexOf(n) < 0) { ppl.push(n); $("#tr-name").value = ""; renderP(); renderE(); calc3(); } };
    $("#tr-name").addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); $("#tr-add-p").click(); } });
    $("#tr-add-e").onclick = function () { if (!ppl.length) return; exps.push([ppl[0], 0, ""]); renderE(); calc3(); };
    var calc3 = function () {
      var total = exps.reduce(function (s, e) { return s + e[1]; }, 0), share = ppl.length ? total / ppl.length : 0, bal = {};
      ppl.forEach(function (p) { bal[p] = -share; }); exps.forEach(function (e) { if (bal[e[0]] !== undefined) bal[e[0]] += e[1]; });
      var cr = [], dr = []; Object.keys(bal).forEach(function (p) { var v = Math.round(bal[p] * 100) / 100; if (v > 0.004) cr.push([p, v]); else if (v < -0.004) dr.push([p, -v]); });
      cr.sort(function (a, b) { return b[1] - a[1]; }); dr.sort(function (a, b) { return b[1] - a[1]; });
      var tx = [], i = 0, j = 0;
      while (i < dr.length && j < cr.length) { var m = Math.min(dr[i][1], cr[j][1]); tx.push(dr[i][0] + " pays " + cr[j][0] + " " + money(m)); dr[i][1] -= m; cr[j][1] -= m; if (dr[i][1] < 0.005) i++; if (cr[j][1] < 0.005) j++; }
      $("#tr-each").textContent = money(share);
      $("#tr-out").innerHTML = "<tr><td>Trip total</td><td>" + money(total) + "</td></tr>" + Object.keys(bal).map(function (p) { return "<tr><td>" + esc(p) + " balance</td><td>" + (bal[p] >= 0 ? "+" : "") + money(bal[p]) + "</td></tr>"; }).join("");
      $("#tr-tx").textContent = tx.length ? tx.join("\n") : "Everyone is settled up.";
    };
    renderP(); renderE(); calc3();
  }

  /* ---------- Subscription audit ---------- */
  var sa = $("#tool-subs");
  if (sa) {
    var sl = $("#sa-list");
    var addS = function (n, c, f, k) {
      var d = document.createElement("div"); d.className = "item-row";
      d.innerHTML = '<input placeholder="Subscription" value="' + esc(n || "") + '" aria-label="Name"><input type="number" min="0" step="0.01" placeholder="Cost" value="' + (c || "") + '" aria-label="Cost"><select aria-label="Billing"><option value="4.345">weekly</option><option value="1" selected>monthly</option><option value="0.0833333">yearly</option></select><label class="check" style="margin:0"><input type="checkbox" ' + (k === false ? "" : "checked") + '> keep</label>';
      if (f) $("select", d).value = f; sl.appendChild(d);
    };
    [["Video streaming", 15.49], ["Music", 10.99], ["Cloud storage", 2.99], ["Gym", 39.99], ["News app", 4.99, "1", false], ["Design tool", 119.99, "0.0833333"]].forEach(function (s) { addS(s[0], s[1], s[2], s[3]); });
    $("#sa-add").onclick = function () { addS(); calc4(); };
    var calc4 = function () {
      var m = 0, cut = 0;
      $$(".item-row", sl).forEach(function (r) { var c = num($$("input", r)[1]) * num($("select", r).value); m += c; if (!$('input[type="checkbox"]', r).checked) cut += c; });
      var fv = function (pm) { var r = 0.07 / 12, n = 120; return pm * ((Math.pow(1 + r, n) - 1) / r); };
      $("#sa-year").textContent = money(m * 12);
      $("#sa-out").innerHTML = "<tr><td>Monthly</td><td>" + money(m) + "</td></tr><tr><td>Per day</td><td>" + money(m * 12 / 365) + "</td></tr><tr><td>Cancelling unchecked saves / yr</td><td>" + money(cut * 12) + "</td></tr><tr><td>…invested 10 yrs @7%</td><td>" + money(fv(cut)) + "</td></tr>";
    };
    live(sa, calc4);
  }
})();
