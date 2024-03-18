var selectedRow = null;

function onFormSubmit() {
    if (validate()) {
        var formData = readFormData();
        if (selectedRow == null)
            insertNewRecord(formData);
        else
            updateRecord(formData);
        resetForm();
    }
}

function readFormData() {
    var formData = {};
    formData["fullName"] = document.getElementById("fullName").value;
    // Leia os outros campos (email, salário, cidade) aqui
    return formData;
}

function insertNewRecord(data) {
    var table = document.getElementById("employeeList").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    // Insira os dados nas células da nova linha
    // Adicione botões de edição e exclusão
}

function resetForm() {
    document.getElementById("fullName").value = "";
    // Limpe os outros campos (email, salário, cidade) aqui
    selectedRow = null;
}

// Implemente as funções onEdit, updateRecord e onDelete

function validate() {
    var isValid = true;
    if (document.getElementById("fullName").value == "") {
        isValid = false;
        document.getElementById("fullNameValidationError").classList.remove("hide");
    } else {
        isValid = true;
        if (!document.getElementById("fullNameValidationError").classList.contains("hide"))
            document.getElementById("fullNameValidationError").classList.add("hide");
    }
    return isValid;
}