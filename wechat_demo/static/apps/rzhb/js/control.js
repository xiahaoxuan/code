function createProvideWater() {
	var html;
	for (var i = 0; i < 7; i++) {
		// 供水时间
		if (variable_water) {
			var body = $('<tbody><tr><td style="width:4em">生效</td><td>起始时间</td><td>结束时间</td><td>智能</td></tr></tbody>');
		} else {
			var body = $('<tbody><tr><td style="width:4em">生效</td><td>起始时间</td><td>结束时间</td></tr></tbody>');
		}
		for (var j = 0; j < 5; j++) {
			html =  '';
			html += '<tr>';
			html += '	<td style="text-align:center">';
			html += '		<label class="csscheckbox">';
			html += '			<input type="checkbox" class="form-control group-Params" id="ProvideWater_Valid_Week'+i+'_Idx'+j+'" data-type="checkbox"><span></span>';
			html += '		</label>';
			html += '	</td>';
			html += '	<td>';
			html += '		<div class="input-group bootstrap-timepicker">';
			html += '			<input type="text" class="form-control input-timepicker24 group-Params" id="ProvideWater_OnTime_Week'+i+'_Idx'+j+'" data-type="timepicker">';
			html += '		</div>';
			html += '	</td>';
			html += '	<td>';
			html += '		<div class="input-group bootstrap-timepicker">';
			html += '			<input type="text" class="form-control input-timepicker24 group-Params" id="ProvideWater_OffTime_Week'+i+'_Idx'+j+'" data-type="timepicker">';
			html += '		</div>';
			html += '	</td>';
			if (variable_water) {
				html += '	<td style="text-align:center">';
				html += '		<label class="csscheckbox">';
				html += '			<input type="checkbox" class="form-control group-Params" id="ProvideWater_AI_Week'+i+'_Idx'+j+'" data-type="checkbox"><span></span>';
				html += '		</label>';
				html += '	</td>';
			}
			html += '</tr>';
			body.append($(html));
		}
		var week = $('<div id="time-pw-week'+i+'" class="tab-pane'+ (i == 0 ? ' active' : '') +'"><form class="form-horizontal form-bordered" style="margin:0;"><table class="table table-striped table-bordered table-vcenter">' + body.html() + '</table></from></div>');
		$("#ProvideWater").append(week);
	}
}

function createAddWater() {
	var html;
	for (var i = 0; i < 7; i++) {
		// 供水时间
		var body = $('<tbody><tr><td style="width:4em">生效</td><td>起始时间</td><td>结束时间</td><td style="width:120px;">加水模式</td><td style="width:120px;">水位上限</td><td style="width:120px;">水位下限</td></tr></tbody>');
		for (var j = 0; j < 5; j++) {
			html =  '';
			html += '<tr>';
			html += '	<td style="text-align:center">';
			html += '		<label class="csscheckbox">';
			html += '			<input type="checkbox" class="form-control group-Params" id="AddWater_Valid_Week'+i+'_Idx'+j+'" data-type="checkbox"><span></span>';
			html += '		</label>';
			html += '	</td>';
			html += '	<td>';
			html += '		<div class="input-group bootstrap-timepicker">';
			html += '			<input type="text" class="form-control input-timepicker24 group-Params" id="AddWater_OnTime_Week'+i+'_Idx'+j+'" data-type="timepicker">';
			html += '		</div>';
			html += '	</td>';
			html += '	<td>';
			html += '		<div class="input-group bootstrap-timepicker">';
			html += '			<input type="text" class="form-control input-timepicker24 group-Params" id="AddWater_OffTime_Week'+i+'_Idx'+j+'" data-type="timepicker">';
			html += '		</div>';
			html += '	</td>';
			html += '	<td>';
			html += '		<select class="form-control group-Params" id="AddWater_Mode_Week'+i+'_Idx'+j+'" data-type="value">';
			html += '			<option value="0">直接加水</option>';
			html += '			<option value="1">温差加水</option>';
			html += '		</select>';
			html += '	</td>';
			html += '	<td>';
			html += '		<div class="input-group input_number">';
			html += '			<input type="number" class="form-control group-Params" id="AddWater_LevelTop_Week'+i+'_Idx'+j+'" data-type="value">';
			html += '			<span class="input-group-addon">米</span>';
			html += '		</div>';
			html += '	</td>';
			html += '	<td>';
			html += '		<div class="input-group input_number">';
			html += '			<input type="number" class="form-control group-Params" id="AddWater_LevelBottom_Week'+i+'_Idx'+j+'" data-type="value">';
			html += '			<span class="input-group-addon">米</span>';
			html += '		</div>';
			html += '	</td>';
			html += '</tr>';
			body.append($(html));
		}
		var week = $('<div id="time-aw-week'+i+'" class="tab-pane'+ (i == 0 ? ' active' : '') +'"><form class="form-horizontal form-bordered" style="margin:0;"><div class="table-responsive"><table class="table table-striped table-bordered table-vcenter" style="min-width:608px;">' + body.html() + '</table></div></from></div>');
		$("#AddWater").append(week);
	}
}

function createAddWater2() {
	var html;
	for (var i = 0; i < 7; i++) {
		// 供水时间
		var body = $('<tbody><tr><td style="width:4em">生效</td><td>起始时间</td><td>结束时间</td><td style="width:120px;">加水模式</td><td style="width:120px;">水位上限</td><td style="width:120px;">水位下限</td></tr></tbody>');
		for (var j = 0; j < 5; j++) {
			html =  '';
			html += '<tr>';
			html += '	<td style="text-align:center">';
			html += '		<label class="csscheckbox">';
			html += '			<input type="checkbox" class="form-control group-Params" id="AddWater2_Valid_Week'+i+'_Idx'+j+'" data-type="checkbox"><span></span>';
			html += '		</label>';
			html += '	</td>';
			html += '	<td>';
			html += '		<div class="input-group bootstrap-timepicker">';
			html += '			<input type="text" class="form-control input-timepicker24 group-Params" id="AddWater2_OnTime_Week'+i+'_Idx'+j+'" data-type="timepicker">';
			html += '		</div>';
			html += '	</td>';
			html += '	<td>';
			html += '		<div class="input-group bootstrap-timepicker">';
			html += '			<input type="text" class="form-control input-timepicker24 group-Params" id="AddWater2_OffTime_Week'+i+'_Idx'+j+'" data-type="timepicker">';
			html += '		</div>';
			html += '	</td>';
			html += '	<td>';
			html += '		<select class="form-control group-Params" id="AddWater2_Mode_Week'+i+'_Idx'+j+'" data-type="value">';
			html += '			<option value="0">直接加水</option>';
			html += '			<option value="1">温差加水</option>';
			html += '		</select>';
			html += '	</td>';
			html += '	<td>';
			html += '		<div class="input-group input_number">';
			html += '			<input type="number" class="form-control group-Params" id="AddWater2_LevelTop_Week'+i+'_Idx'+j+'" data-type="value">';
			html += '			<span class="input-group-addon">米</span>';
			html += '		</div>';
			html += '	</td>';
			html += '	<td>';
			html += '		<div class="input-group input_number">';
			html += '			<input type="number" class="form-control group-Params" id="AddWater2_LevelBottom_Week'+i+'_Idx'+j+'" data-type="value">';
			html += '			<span class="input-group-addon">米</span>';
			html += '		</div>';
			html += '	</td>';
			html += '</tr>';
			body.append($(html));
		}
		var week = $('<div id="time-aw2-week'+i+'" class="tab-pane'+ (i == 0 ? ' active' : '') +'"><form class="form-horizontal form-bordered" style="margin:0;"><div class="table-responsive"><table class="table table-striped table-bordered table-vcenter" style="min-width:608px;">' + body.html() + '</table></div></from></div>');
		$("#AddWater2").append(week);
	}
}