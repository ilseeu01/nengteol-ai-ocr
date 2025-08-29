import FoodUpload from "../components/FoodUpload/FoodUpload";

export default function MyFridgeUpload() {
    return (
        <div className="space-y-6">
            <FoodUpload apiUrl="http://223.130.140.174:5000/api/foods" />
        </div>
    );
}
